% Reproduce the analytical equation surface from MMT_TEModeling.
%
% This MATLAB script mirrors the Python implementation in
% mmt_te_modeling_reproduction.py. It implements the paper equation groups
% and runs one RV-80E demonstration with transparent equivalent-error values.
%
% The demo is an executable equation-chain check, not exact reproduction of
% the paper figures. Exact figure reproduction requires reducer-specific
% cycloidal contact geometry and measured component errors for every sample.

clear;
clc;

parameters = build_reducer_parameters();
errors = build_equivalent_errors();
sample_count = 11440;

[theta_h_rad, rte_rad] = run_rv80e_demo(parameters, errors, sample_count);
print_demo_summary(rte_rad);

function parameters = build_reducer_parameters()
    parameters.z1 = 10;
    parameters.z2 = 38;
    parameters.z4 = 39;
    parameters.z5 = 40;
    parameters.module_mm = 1.75;
    parameters.pressure_angle_rad = deg2rad(20.0);
    parameters.pin_pitch_radius_mm = 77.5;
    parameters.crank_eccentricity_mm = 1.5;
    parameters.pin_radius_mm = 4.0;
    parameters.carrier_radius_mm = 0.5 * parameters.module_mm * (parameters.z1 + parameters.z2);
    parameters.sun_base_radius_mm = 0.5 * parameters.module_mm * parameters.z1 * cos(parameters.pressure_angle_rad);
    parameters.planetary_base_radius_mm = 0.5 * parameters.module_mm * parameters.z2 * cos(parameters.pressure_angle_rad);
    parameters.normal_link_length_mm = sqrt(max(parameters.carrier_radius_mm^2 - (parameters.planetary_base_radius_mm - parameters.sun_base_radius_mm)^2, eps));
    parameters.whole_machine_ratio = (parameters.z2 * parameters.z5 + parameters.z1 * (parameters.z5 - parameters.z4)) / (parameters.z1 * (parameters.z5 - parameters.z4));
end

function errors = build_equivalent_errors()
    errors.delta_l_b1_mm = 0.0;
    errors.delta_l_b2_mm = 0.005;
    errors.delta_l_h_mm = 0.004;
    errors.delta_l_c_mm = 0.005;
    errors.delta_l_a_mm = 0.003;
    errors.delta_l_v_mm = 0.0;
    errors.delta_l_r_mm = 0.005;
    errors.accumulative_pitch_error_mm = 0.005;
    errors.cycloidal_profile_error_mm = 0.005;
    errors.pin_radius_error_mm = 0.002;
    errors.delta_theta_b1_rad = 0.0;
    errors.curvature_radius_positive = true;
end

function [theta_h_rad, theta_3_rad] = output_and_crank_angles(theta_1_rad, parameters)
    denominator = parameters.z2 * parameters.z5 + parameters.z1 * (parameters.z5 - parameters.z4);
    theta_h_rad = parameters.z1 * (parameters.z5 - parameters.z4) / denominator .* theta_1_rad;
    theta_3_rad = -parameters.z4 / (parameters.z5 - parameters.z4) .* theta_h_rad;
end

function [theta_ai_rad, theta_hi_rad] = parallelogram_angles(theta_h_rad, theta_3_rad)
    theta_a_rad = 2.0 * pi - theta_3_rad;
    loop_offsets_rad = [0.0, 2.0 * pi / 3.0, 4.0 * pi / 3.0];
    theta_hi_rad = theta_h_rad(:) + pi / 2.0 + loop_offsets_rad;
    theta_ai_rad = repmat(theta_a_rad(:), 1, 3);
end

function [theta_b1_rad, theta_n_rad, theta_b2_rad] = involute_linkage_angles(theta_h1_rad, pressure_angle_rad)
    theta_b1_rad = theta_h1_rad - pressure_angle_rad;
    theta_n_rad = theta_h1_rad - pressure_angle_rad + pi / 2.0;
    theta_b2_rad = theta_h1_rad - pressure_angle_rad + pi;
end

function theta_p_rad = pin_angle(pin_index, pin_count)
    theta_p_rad = (double(pin_index) - 1.0) .* 2.0 * pi / pin_count;
end

function [x_k_mm, y_k_mm, x_o4_mm, y_o4_mm] = pin_and_cycloid_centers(theta_p_rad, theta_a_rad, parameters)
    x_k_mm = parameters.pin_pitch_radius_mm .* cos(theta_p_rad);
    y_k_mm = parameters.pin_pitch_radius_mm .* sin(theta_p_rad);
    x_o4_mm = parameters.crank_eccentricity_mm .* cos(theta_a_rad);
    y_o4_mm = parameters.crank_eccentricity_mm .* sin(theta_a_rad);
end

function [theta_rho_rad, theta_k_rad] = contact_linkage_angles(x_c_mm, y_c_mm, x_k_mm, y_k_mm, x_o4_mm, y_o4_mm)
    theta_rho_rad = atan2(y_k_mm - y_c_mm, x_k_mm - x_c_mm);
    theta_k_rad = atan2(y_c_mm - y_o4_mm, x_c_mm - x_o4_mm);
end

function denominator = safe_sin(angle_rad)
    denominator = sin(angle_rad);
    minimum_safe_sine = 5.0e-2;
    small_mask = abs(denominator) < minimum_safe_sine;
    denominator(small_mask) = sign(denominator(small_mask) + eps) * minimum_safe_sine;
end

function delta_angle_rad = angle_difference(theta_x_rad, theta_y_rad)
    delta_angle_rad = theta_x_rad - theta_y_rad;
end

function [delta_theta_c_rad, delta_l_k_mm, delta_l_rho_mm] = cycloid_profile_pin_radius_errors(theta_k_rho_rad, errors)
    denominator = safe_sin(theta_k_rho_rad);
    combined_error_mm = errors.cycloidal_profile_error_mm + errors.pin_radius_error_mm;
    if errors.curvature_radius_positive
        curvature_exponent = 0;
    else
        curvature_exponent = 1;
    end
    delta_theta_c_rad = combined_error_mm ./ denominator;
    delta_l_k_mm = ((-1.0) ^ curvature_exponent) .* combined_error_mm ./ (denominator .^ 2) .* cos(theta_k_rho_rad);
    delta_l_rho_mm = ((-1.0) ^ (curvature_exponent + 1)) .* combined_error_mm ./ (denominator .^ 2);
end

function [delta_l_h_mm, delta_l_v_mm] = output_disc_assembly_errors(output_disc_error_mm, output_disc_error_angle_rad, theta_h_rad, theta_v_rad)
    delta_l_h_mm = -output_disc_error_mm .* cos(output_disc_error_angle_rad - theta_h_rad);
    delta_l_v_mm = -output_disc_error_mm .* cos(output_disc_error_angle_rad - theta_v_rad);
end

function rte_rad = measured_rte(theta_h_rad, theta_1_rad, speed_ratio)
    rte_rad = theta_h_rad - theta_1_rad ./ speed_ratio;
end

function [f1, f2i, f3, f4i] = compute_subsystem_errors(parameters, errors, theta_b1_rad, theta_n_rad, theta_b2_rad, theta_h1_rad, theta_hi_rad, theta_ai_rad, theta_v_rad, theta_ci_rad, theta_k_rad, theta_rho_rad, theta_p_rad, delta_l_k_mm, delta_l_rho_mm)
    l_b1_mm = parameters.sun_base_radius_mm;
    l_b2_mm = parameters.planetary_base_radius_mm;
    l_h_mm = parameters.carrier_radius_mm;
    l_v_mm = parameters.crank_eccentricity_mm;
    l_k_mm = max(parameters.pin_radius_mm, eps);

    theta_b1_n_rad = angle_difference(theta_b1_rad, theta_n_rad);
    theta_h1_n_rad = angle_difference(theta_h1_rad, theta_n_rad);
    theta_b2_n_rad = angle_difference(theta_b2_rad, theta_n_rad);
    delta_l_n_mm = errors.delta_l_b1_mm .* cos(theta_b1_rad - theta_n_rad) + errors.delta_l_b2_mm .* cos(theta_b2_rad - theta_n_rad);
    f1 = (-errors.delta_l_b1_mm / l_b2_mm .* cos(theta_b1_n_rad) + l_b1_mm / l_b2_mm .* errors.delta_theta_b1_rad .* sin(theta_b1_n_rad) - delta_l_n_mm / l_b2_mm + errors.delta_l_h_mm / l_b2_mm .* cos(theta_h1_n_rad) + errors.delta_l_b2_mm / l_b2_mm .* cos(theta_b2_n_rad)) ./ safe_sin(theta_b2_n_rad);

    theta_v_ci_rad = angle_difference(theta_v_rad(:), theta_ci_rad);
    theta_hi_ci_rad = angle_difference(theta_hi_rad, theta_ci_rad);
    theta_ai_ci_rad = angle_difference(theta_ai_rad, theta_ci_rad);
    f2i = (-errors.delta_l_h_mm / l_v_mm .* cos(theta_hi_ci_rad) - errors.delta_l_a_mm / l_v_mm .* cos(theta_ai_ci_rad) + errors.delta_l_v_mm / l_v_mm .* cos(theta_v_ci_rad) + errors.delta_l_c_mm / l_v_mm) ./ safe_sin(theta_v_ci_rad);

    theta_v_rho_rad = angle_difference(theta_v_rad, theta_rho_rad);
    theta_k_rho_rad = angle_difference(theta_k_rad, theta_rho_rad);
    theta_p_rho_rad = angle_difference(theta_p_rad, theta_rho_rad);
    delta_theta_p_rad = errors.accumulative_pitch_error_mm .* sin(theta_p_rad) ./ parameters.pin_pitch_radius_mm;
    f3 = (errors.delta_l_v_mm / l_k_mm .* cos(theta_v_rho_rad) + delta_l_k_mm / l_k_mm .* cos(theta_k_rho_rad) + delta_l_rho_mm / l_k_mm - errors.delta_l_r_mm / l_k_mm .* cos(theta_p_rho_rad) + parameters.pin_pitch_radius_mm / l_k_mm .* delta_theta_p_rad .* sin(theta_p_rho_rad)) ./ safe_sin(theta_k_rho_rad);

    theta_hi_ai_rad = angle_difference(theta_hi_rad, theta_ai_rad);
    theta_v_ai_rad = angle_difference(theta_v_rad(:), theta_ai_rad);
    theta_ci_ai_rad = angle_difference(theta_ci_rad, theta_ai_rad);
    f4i = (errors.delta_l_h_mm / l_h_mm .* cos(theta_hi_ai_rad) + errors.delta_l_a_mm / l_h_mm - errors.delta_l_v_mm / l_h_mm .* cos(theta_v_ai_rad) - errors.delta_l_c_mm / l_h_mm .* cos(theta_ci_ai_rad)) ./ safe_sin(theta_hi_ai_rad);
end

function rte_rad = whole_machine_rte_universal(f1, f2i, f3, f4i, parameters)
    g1 = -(parameters.z1 + parameters.z2) / parameters.z2;
    g2 = 1.0;
    g3 = -(parameters.z5 - parameters.z4) / parameters.z4;
    g4 = 1.0;
    denominator = 1.0 + g1 * g2 * g3 * g4;
    rte_rad = g2 * g3 * g4 / denominator .* f1 + g3 * g4 / denominator .* mean(f2i, 2) + g4 / denominator .* f3 + 1.0 / denominator .* mean(f4i, 2);
end

function rte_rad = whole_machine_rte_one_tooth(f1, f2i, f3, f4i, parameters)
    numerator = -1.0 / parameters.z4 .* f1 - 1.0 / (3.0 * parameters.z4) .* sum(f2i, 2) + f3 + 1.0 / 3.0 .* sum(f4i, 2);
    denominator = 1.0 + (parameters.z1 + parameters.z2) / (parameters.z2 * parameters.z4);
    rte_rad = numerator ./ denominator;
end

function [theta_h_rad, rte_rad] = run_rv80e_demo(parameters, errors, sample_count)
    theta_h_rad = linspace(0.0, 2.0 * pi, sample_count + 1)';
    theta_h_rad = theta_h_rad(1:end-1);
    theta_1_rad = theta_h_rad .* parameters.whole_machine_ratio;
    [theta_h_from_input_rad, theta_3_rad] = output_and_crank_angles(theta_1_rad, parameters);
    [theta_ai_rad, theta_hi_rad] = parallelogram_angles(theta_h_from_input_rad, theta_3_rad);
    [theta_b1_rad, theta_n_rad, theta_b2_rad] = involute_linkage_angles(theta_hi_rad(:, 1), parameters.pressure_angle_rad);

    pin_indices = mod((0:sample_count-1)', parameters.z5) + 1;
    theta_p_rad = pin_angle(pin_indices, parameters.z5);
    theta_v_rad = theta_ai_rad(:, 1);
    theta_ci_rad = theta_hi_rad + pi / 5.0;
    [~, ~, ~, ~] = pin_and_cycloid_centers(theta_p_rad, theta_v_rad, parameters);
    theta_rho_rad = theta_p_rad - pi / 5.0;
    theta_k_rad = theta_p_rad + pi / 5.0;

    theta_k_rho_rad = angle_difference(theta_k_rad, theta_rho_rad);
    [~, delta_l_k_mm, delta_l_rho_mm] = cycloid_profile_pin_radius_errors(theta_k_rho_rad, errors);
    [f1, f2i, f3, f4i] = compute_subsystem_errors(parameters, errors, theta_b1_rad, theta_n_rad, theta_b2_rad, theta_hi_rad(:, 1), theta_hi_rad, theta_ai_rad, theta_v_rad, theta_ci_rad, theta_k_rad, theta_rho_rad, theta_p_rad, delta_l_k_mm, delta_l_rho_mm);
    rte_rad = whole_machine_rte_one_tooth(f1, f2i, f3, f4i, parameters);
end

function print_demo_summary(rte_rad)
    arcsecond_per_radian = 180.0 * 3600.0 / pi;
    rte_arcsec = rte_rad .* arcsecond_per_radian;
    fprintf("MMT_TEModeling analytical equation-chain demo\n");
    fprintf("Samples: %d\n", numel(rte_arcsec));
    fprintf("RTE arcsec min/max: %.6f / %.6f\n", min(rte_arcsec), max(rte_arcsec));
    fprintf("RTE arcsec peak-to-peak: %.6f\n", peak2peak(rte_arcsec));

    centered_rte_arcsec = rte_arcsec - mean(rte_arcsec);
    spectrum = fft(centered_rte_arcsec);
    amplitude = 2.0 .* abs(spectrum) ./ numel(centered_rte_arcsec);
    positive_amplitude = amplitude(2:floor(numel(amplitude) / 2));
    [sorted_amplitude, sorted_index] = sort(positive_amplitude, "descend");
    fprintf("Dominant demonstration harmonic bins:\n");
    for index = 1:min(8, numel(sorted_index))
        fprintf("  h=%d amplitude_arcsec=%.6f\n", sorted_index(index), sorted_amplitude(index));
    end
end
