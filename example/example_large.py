#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021 Kotaro Terada
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rectangle_packing_solver as rps


def main():
    # Define a problem
    problem = rps.Problem(rectangles=[(0.1 * i, 0.1 * i) for i in range(100, 200, 5)])
    print("problem:", problem)

    # Find a solution
    solution = rps.Solver().solve(problem=problem, simanneal_minutes=1.0, simanneal_steps=500)
    print("solution:", solution)

    # Visualization (to floorplan.png)
    rps.Visualizer().visualize(solution=solution, path="./figs/floorplan_large.png")


if __name__ == "__main__":
    main()
