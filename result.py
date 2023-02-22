#!/usr/bin/python
import os

from picods import picoplot
from picods import picotable
from pyaon.knapsack import load as read_knapsack
from pydaa.dynamic_programming import knapsack as dynamic_knapsack
from pydaa.greedy import knapsack as greedy_knapsack


def main():
    data = list(
        map(
            lambda x: [
                x["size"],
                x["dynamic"][0].microseconds,
                x["greedy"][0].microseconds,
                x["dynamic"][1],
                x["greedy"][1],
            ],
            map(
                lambda x: {
                    "size":
                    x["size"],
                    "dynamic":
                    dynamic_knapsack(x["data"][0], x["data"][1], x["data"][2]),
                    "greedy":
                    greedy_knapsack(x["data"][0], x["data"][1], x["data"][2]),
                },
                sorted(
                    map(
                        lambda x: {
                            "size": int("".join(filter(str.isdigit, x))),
                            "data": read_knapsack(f"./data/{x}"),
                        },
                        os.listdir("data"),
                    ),
                    key=lambda x: x["size"],
                ),
            ),
        ))

    picotable(
        "Knapsack Results",
        data,
        [
            "Size",
            "Dynamic Time(μs)",
            "Greedy Time(μs)",
            "Dynamic Result",
            "Greedy Result",
        ],
        ["" for i in range(len(data))],
    )

    picoplot(
        "Knapsack Execution times - Comparsion",
        [
            [i[1] for i in data],
            [i[2] for i in data],
        ],
        [[i[0] for i in data], [i[0] for i in data]],
        ["Dynamic", "Greedy"],
        ["red", "blue"],
        "Size",
        "Time(μs)",
    )

    picoplot(
        "Knapsack Execution times - Dynamic",
        [
            [i[1] for i in data],
        ],
        [[i[0] for i in data]],
        ["Dynamic"],
        ["red"],
        "Size",
        "Time(μs)",
    )

    picoplot(
        "Knapsack Execution times - Greedy",
        [
            [i[2] for i in data],
        ],
        [[i[0] for i in data]],
        ["Greedy"],
        ["blue"],
        "Size",
        "Time(μs)",
    )


if __name__ == "__main__":
    main()
