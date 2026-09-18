from __future__ import annotations

import argparse
import json
from pathlib import Path

from deptos.fixtures import ensure_fixtures
from deptos.runtime import DeptOS

ROOT = Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DeptOS multi-department agent runtime")
    p.add_argument("request", nargs="?", default=(
        "Prepare Monday exec briefing: reconcile training vs PA matrix, "
        "flag inbox items that block certification, draft weekly status."
    ))
    p.add_argument("--fixtures", type=Path, default=ROOT / "fixtures")
    p.add_argument("--runs", type=Path, default=ROOT / "runs")
    args = p.parse_args(argv)
    ensure_fixtures(args.fixtures)
    packet = DeptOS(args.fixtures, args.runs).handle(args.request)
    print(f"run_id={packet.run_id}")
    print(f"status={packet.status}")
    print(f"findings={len(packet.findings)} decisions={len(packet.decisions)} events={len(packet.events)}")
    if packet.audit_notes:
        print("AUDIT:")
        for n in packet.audit_notes:
            print(f"  - {n}")
    print()
    print(packet.briefing_md)
    print(f"trace: {args.runs / (packet.run_id + '.jsonl')}")
    print(f"packet: {args.runs / (packet.run_id + '.packet.json')}")
    print("JSON:" + json.dumps({"run_id": packet.run_id, "status": packet.status, "findings": len(packet.findings)}))
    return 0 if packet.status == "ready_for_human" else 2


if __name__ == "__main__":
    raise SystemExit(main())
