def get_valid_input(prompt, default=None):
    while True:
        x = input(prompt)
        if x == '':
            if default is None:
                print('Invalid input. Enter again.')
                continue
            x = default
        try:
            x = float(x)
            break
        except:
            print('Invalid input. Enter again.')
    return x


if __name__ == '__main__':

    weight_dist = get_valid_input('Enter Weight Distribution (in %): ') / 100

    antiroll_f_max = get_valid_input('Enter Antiroll Bar Front Max (65): ', 65)

    antiroll_f_min = get_valid_input('Enter Antiroll Bar Front Min (1): ', 1)

    antiroll_r_max = get_valid_input(f'Enter Antiroll Bar Rear Max ({antiroll_f_max}): ', antiroll_f_max)

    antiroll_r_min = get_valid_input(f'Enter Antiroll Bar Rear Min ({antiroll_f_min}): ', antiroll_f_min)

    spring_f_max = get_valid_input('Enter Spring Front Max: ')

    spring_f_min = get_valid_input('Enter Spring Front Min: ')

    spring_r_max = get_valid_input(f'Enter Spring Rear Max ({spring_f_max}): ', spring_f_max)

    spring_r_min = get_valid_input(f'Enter Spring Rear Min ({spring_f_min}): ', spring_f_min)

    damping_f_max = get_valid_input(f'Enter Damping Front Max (20): ', 20)

    damping_f_min = get_valid_input(f'Enter Damping Front Min (3): ', 3)

    damping_r_max = get_valid_input(f'Enter Damping Rear Max ({damping_f_max}): ', damping_f_max)

    damping_r_min = get_valid_input(f'Enter Damping Rear Min ({damping_f_min}): ', damping_f_min)

    # Output
    print("\nOutput:")
    print(f'Antiroll Bar Front: {round(((antiroll_f_max - antiroll_f_min) * weight_dist + antiroll_f_min), 2)}')
    print(f'Antiroll Bar Rear: {round(((antiroll_r_max - antiroll_r_min) * (1 - weight_dist) + antiroll_r_min), 2)}')
    print(f'Spring Front: {round(((spring_f_max - spring_f_min) * weight_dist + spring_f_min), 1)}')
    print(f'Spring Rear: {round(((spring_r_max - spring_r_min) * (1 - weight_dist) + spring_r_min), 1)}')
    print(f'Rebound Stiffness Front: {round(((damping_f_max - damping_f_min) * weight_dist + damping_f_min), 1)}')
    print(f'Rebound Stiffness Rear: {round(((damping_r_max - damping_r_min) * (1 - weight_dist) + damping_r_min), 1)}')
    print(
        f'Bump Stiffness Front: {round((((damping_f_max - damping_f_min) * weight_dist + damping_f_min) * 0.6), 1)}')
    print(
        f'Bump Stiffness Rear: {round((((damping_r_max - damping_r_min) * (1 - weight_dist) + damping_r_min) * 0.6), 1)}')
