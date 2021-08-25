from argparse import ArgumentParser


def main(args):
    print_results(args)


def bmi_calc(weight_kg, height_m):
    """Calculate BMI from weight in kg and height in meters"""
    bmi = int(weight_kg / height_m ** 2)
    return bmi


def predict_max_HR(age):
    """Age predicted maximal heart rate"""
    max_HR = 208 - 0.7 * age
    return max_HR


def bp_risk(systolic, diastolic):
    """Categorises whether blood pressure is elevated,
 stage 1 hypertension or stage 2 hypertension"""
    if systolic >= 120 and systolic < 130 and diastolic < 80:
        bprisk = 'elevated BP'
    elif (systolic >= 130 and systolic < 140) or (diastolic >= 80 and diastolic < 90):
        bprisk = 'stage 1 hypertension'
    elif systolic >= 140 or diastolic >= 90:
        bprisk = 'stage 2 hypertension'
    else:
        bprisk = 'invalid values'
    return bprisk


def print_results(args):
    bmi = bmi_calc(args.weight, args.height)
    if args.greeting:
        print('\nGreat job! Thinking of your fitness is a great thing to do for yourself.')
    print("\n\t")
    if args.initials:
        print(args.initials)
    print("\tweight = {} kg".format(args.weight))
    print("\theight = {} m".format(args.height))
    print("\tbmi = {:3.1f}".format(bmi))
    if args.age:
        print("\tage = {} years old".format(args.age))
        max_HR = predict_max_HR(args.age)
        print("\tpredicted maximal heart rate = {} bpm".format(max_HR))
    if args.systolic and args.diastolic:
        bprisk = bp_risk(args.systolic, args.diastolic)
        print("\tblood pressure = {}/{}".format(args.systolic, args.diastolic))
        print("\tblood presure = " + bprisk)
    print("\n")


if __name__ == "__main__":
    USAGE = """fitness_argparse v0.1

        Created by Martin Héroux (heroux.martin at gmail.com)

        Determines fitness level based on a few simple inputs.
        
        USAGE:
        
        $ python fitness_argparse.py 70 1.75 --age 40 --systolic 135 --diastolic 82
        """
    parser = ArgumentParser(description=USAGE)
    parser.add_argument(
        "weight",
        type=float,
        default=None,
        help="Person's weight in Kg",
    )
    parser.add_argument(
        "height",
        type=float,
        default=None,
        help="Person's height in metres",
    )
    parser.add_argument(
        "-i",
        "--initials",
        type=str,
        default=None,
        help="Initials of person",
    )
    parser.add_argument(
        "-a",
        "--age",
        type=int,
        help="Person's age",
    )
    parser.add_argument(
        "-s",
        "--systolic",
        type=int,
        help="Person's systolic blood pressure",
    )
    parser.add_argument(
        "-d",
        "--diastolic",
        type=int,
        help="Person's diastolic blood pressure",
    )
    parser.add_argument(
        "-g",
        "--greeting",
        action="store_true",
        help="Provide a brief greeting to user",
    )
    args = parser.parse_args()
    main(args)
