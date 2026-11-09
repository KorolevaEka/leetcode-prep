import json


def summarize(report_json: str) -> dict[str, list[str]]:
    failed, flaky = [], []
    for result in json.loads(report_json).get("results", []):
        attempts = result["attempts"]
        if attempts[-1] == "failed":
            failed.append(result["name"])
        elif "failed" in attempts:
            flaky.append(result["name"])
    return {"failed": failed, "flaky": flaky}
