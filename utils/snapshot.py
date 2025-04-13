import requests
from datetime import datetime

def ts_to_utc(ts):
    return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M UTC")

def get_status(start_ts, end_ts):
    now = datetime.utcnow().timestamp()
    if now < start_ts:
        return "🕓 Upcoming"
    elif start_ts <= now <= end_ts:
        return "✅ Active"
    else:
        return "❌ Closed"

def get_latest_proposals(space_id, count=3):
    query = """
    query Proposals($space: String!, $first: Int!) {
      proposals(first: $first, skip: 0, where: {space_in: [$space]}, orderBy: "created", orderDirection: desc) {
        id
        title
        start
        end
      }
    }
    """
    url = "https://hub.snapshot.org/graphql"
    response = requests.post(url, json={
        "query": query,
        "variables": {"space": space_id, "first": count}
    })

    proposals = response.json()["data"]["proposals"]
    return [
        {
            "id": p["id"],
            "title": p["title"],
            "start": ts_to_utc(int(p["start"])),
            "end": ts_to_utc(int(p["end"])),
            "status": get_status(int(p["start"]), int(p["end"]))
        } for p in proposals
    ]
