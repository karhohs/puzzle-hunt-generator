import marimo

__generated_with = "0.1.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Puzzle Hunt Generator

        Use this notebook to interactively design and preview individual puzzles.

        ## Getting Started

        1. Import `puzzle_hunt_generator` to access puzzle generators.
        2. Customise puzzle parameters in the cells below.
        3. Run **Generate** to write outputs to the `puzzles/` directory.
        """
    )
    return


@app.cell
def _():
    from puzzle_hunt_generator.hunt import PuzzleHunt
    from puzzle_hunt_generator.puzzle import Puzzle

    hunt = PuzzleHunt(name="My Hunt", output_dir="../puzzles")
    hunt.add_puzzle(Puzzle(name="sample", data={"clue": "What has keys but no locks?", "answer": "a keyboard"}))
    paths = hunt.generate()
    print("Generated:", paths)
    return hunt, paths


if __name__ == "__main__":
    app.run()
