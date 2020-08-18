"""
This script returns the train, dev and test split for AMI corpus
"""

# TODO: Remove sample b4 merge
ALLOWED_OPTIONS = ["scenario_only", "full_corpus", "full_corpus_asr", "sample"]


def get_AMI_split(split_option):
    """Returns train, dev, and test sets for given split_option
    Note: IS1002 (no a), IS1005 (no d)
    """

    if split_option not in ALLOWED_OPTIONS:
        print(
            f'Invalid split "{split_option}" requested!\nValid split_options are: ',
            ALLOWED_OPTIONS,
        )
        return

    # TODO: Remove this before merge
    if split_option == "sample":
        train_set = ["IS1000", "ES2012"]
        dev_set = ["IS1001", "ES2013"]
        # test_set = ["IS1003", "ES2015"]
        test_set = ["IS1003"]

    if split_option == "scenario_only":

        train_set = [
            "ES2002",
            "ES2005",
            "ES2006",
            "ES2007",
            "ES2008",
            "ES2009",
            "ES2010",
            "ES2012",
            "ES2013",
            "ES2015",
            "ES2016",
            "IS1000",
            "IS1001",
            "IS1002",
            "IS1003",
            "IS1004",
            "IS1005",
            "IS1006",
            "IS1007",
            "TS3005",
            "TS3008",
            "TS3009",
            "TS3010",
            "TS3011",
            "TS3012",
        ]

        dev_set = [
            "ES2003",
            "ES2011",
            "IS1008",
            "TS3004",
            "TS3006",
        ]

        test_set = [
            "ES2004",
            "ES2014",
            "IS1009",
            "TS3003",
            "TS3007",
        ]

    if split_option == "full_corpus":
        # List of train: SA (TRAINING PART OF SEEN DATA)
        # Note: IS1002 (no a), IS1005 (no d)
        train_set = [
            "ES2002",
            "ES2005",
            "ES2006",
            "ES2007",
            "ES2008",
            "ES2009",
            "ES2010",
            "ES2012",
            "ES2013",
            "ES2015",
            "ES2016",
            "IS1000",
            "IS1001",
            "IS1002",
            "IS1003",
            "IS1004",
            "IS1005",
            "IS1006",
            "IS1007",
            "TS3005",
            "TS3008",
            "TS3009",
            "TS3010",
            "TS3011",
            "TS3012",
            "EN2001",
            "EN2003",
            "EN2004a",
            "EN2005a",
            "EN2006",
            "EN2009",
            "IN1001",
            "IN1002",
            "IN1005",
            "IN1007",
            "IN1008",
            "IN1009",
            "IN1012",
            "IN1013",
            "IN1014",
            "IN1016",
        ]

        # List of dev: SB (DEV PART OF SEEN DATA)
        dev_set = [
            "ES2003",
            "ES2011",
            "IS1008",
            "TS3004",
            "TS3006",
            "IB4001",
            "IB4002",
            "IB4003",
            "IB4004",
            "IB4010",
            "IB4011",
        ]

        # List of test: SC (UNSEEN DATA FOR EVALUATION)
        # Note that IB4005 does not appear because it has speakers in common with two sets of data.
        test_set = [
            "ES2004",
            "ES2014",
            "IS1009",
            "TS3003",
            "TS3007",
            "EN2002",
        ]

    if split_option == "full_corpus_asr":
        train_set = [
            "ES2002",
            "ES2003",
            "ES2005",
            "ES2006",
            "ES2007",
            "ES2008",
            "ES2009",
            "ES2010",
            "ES2012",
            "ES2013",
            "ES2014",
            "ES2015",
            "ES2016",
            "IS1000",
            "IS1001",
            "IS1002",
            "IS1003",
            "IS1004",
            "IS1005",
            "IS1006",
            "IS1007",
            "TS3005",
            "TS3006",
            "TS3007",
            "TS3008",
            "TS3009",
            "TS3010",
            "TS3011",
            "TS3012",
            "EN2001",
            "EN2003",
            "EN2004a",
            "EN2005a",
            "EN2006",
            "EN2009",
            "IN1001",
            "IN1002",
            "IN1005",
            "IN1007",
            "IN1008",
            "IN1009",
            "IN1012",
            "IN1013",
            "IN1014",
            "IN1016",
        ]

        dev_set = [
            "ES2011",
            "IS1008",
            "TS3004",
            "IB4001",
            "IB4002",
            "IB4003",
            "IB4004",
            "IB4010",
            "IB4011",
        ]

        test_set = [
            "ES2004",
            "IS1009",
            "TS3003",
            "EN2002",
        ]

    return train_set, dev_set, test_set
