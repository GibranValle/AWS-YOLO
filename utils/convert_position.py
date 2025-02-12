def calc_relative_position_2M(pixel_position: tuple[int, int, int, int]):
    # x0, y0, x1, y1
    img_resolution = 1200, 1600
    width = pixel_position[2] - pixel_position[0]
    height = pixel_position[3] - pixel_position[1]
    x_center = pixel_position[0] + width / 2
    y_center = pixel_position[1] + height / 2
    # x_center, y_center, w, h
    pixel_format = (x_center, y_center, width, height)
    relative_position = [
        f"{pixel_format[0] / img_resolution[0]}",
        f"{pixel_format[1] / img_resolution[1]}",
        f"{pixel_format[2] / img_resolution[0]}",
        f"{pixel_format[3] / img_resolution[1]}",
    ]
    return (" ").join(relative_position)

aws_field_calib_button = 975, 1258, 1185, 1340
print("\naws_field_calib_button")
print(calc_relative_position_2M(aws_field_calib_button))

aws_calib_button = 1134, 1388, 1184, 1434
print("\naws_calib_button")
print(calc_relative_position_2M(aws_calib_button))

aws_ok_grey_button = 490, 1467, 598, 1513
print("\naws_ok_grey_button")
print(calc_relative_position_2M(aws_ok_grey_button))

aws_ok_green_button = 538, 929, 661, 1003
print("\naws_ok_green_button")
print(calc_relative_position_2M(aws_ok_green_button))

aws_perform_exposure_2_calibrate = 398, 668, 802, 931
print("\naws_perform_exposure_2_calibrate")
print(calc_relative_position_2M(aws_perform_exposure_2_calibrate))

fpd_calibration_pass = 26, 283, 1516, 1559
print("\nfpd_calibration_pass")
print(calc_relative_position_2M(fpd_calibration_pass))

fpd_calibrating = 26, 411, 1516, 1559
print("\nfpd_calibrating")
print(calc_relative_position_2M(fpd_calibrating))

generator_icon = 1091, 1521, 1160, 1578
print("\ngenerator_icon")
print(calc_relative_position_2M(generator_icon))

generator_text = 26, 1560, 260, 1594
print("\ngenerator_text")
print(calc_relative_position_2M(generator_text))

# mcu_mutl_with = mcu_mutl[2] - mcu_mutl[0]
# mcu_mutl_height = mcu_mutl[3] - mcu_mutl[1]

# new_2 = 282, 282
# mcu_mutl_2 = new_2[0], new_2[1], new_2[0] + mcu_mutl_with, new_2[1] + mcu_mutl_height
# print(calc_relative_position_2M(mcu_mutl_2))

# new_3 = 63, 60
# mcu_mutl_3 = new_3[0], new_3[1], new_3[0] + mcu_mutl_with, new_3[1] + mcu_mutl_height
# print(calc_relative_position_2M(mcu_mutl_3))
