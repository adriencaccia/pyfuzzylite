import fuzzylite as fl


def create() -> fl.Engine:
    return fl.Engine(
        name="ObstacleAvoidance",
        input_variables=[
            fl.InputVariable(
                name="obstacle",
                minimum=0.0,
                maximum=1.0,
                lock_range=False,
                terms=[fl.Ramp("left", 1.0, 0.0), fl.Ramp("right", 0.0, 1.0)],
            )
        ],
        output_variables=[
            fl.OutputVariable(
                name="tsSteer",
                minimum=0.0,
                maximum=1.0,
                lock_range=False,
                lock_previous=False,
                default_value=fl.nan,
                aggregation=fl.Maximum(),
                defuzzifier=fl.WeightedAverage(),
                terms=[fl.Constant("left", 0.333), fl.Constant("right", 0.666)],
            )
        ],
        rule_blocks=[
            fl.RuleBlock(
                name="takagiSugeno",
                conjunction=None,
                disjunction=None,
                implication=None,
                activation=fl.General(),
                rules=[
                    fl.Rule.create("if obstacle is left then tsSteer is right"),
                    fl.Rule.create("if obstacle is right then tsSteer is left"),
                ],
            )
        ],
    )
