"""`arena run --battle battles/B1_ngay_thuong.yaml --seed 42` (đích của `make battle`)."""

import argparse
from pathlib import Path

from arena.scenario import load_battle


def main() -> None:
    p = argparse.ArgumentParser(prog="arena")
    sub = p.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run")
    run.add_argument("--battle", type=Path, required=True)
    run.add_argument("--seed", type=int)
    args = p.parse_args()

    battle = load_battle(args.battle)
    seed = args.seed if args.seed is not None else battle.seed
    print(f"{battle.id} '{battle.title}' seed={seed} runs={battle.runs}")
    # TODO(Block 10): population + faults + recorder theo lịch → oracles → report.
    raise SystemExit("not implemented: battle runner")
