
const dummy_input = [
  {
    "timestamp": "2025-04-25T10:15:00Z",
    "type": "recommendation_sent",
    "session_id": "sess-001",
    "message": "Sent 5 recommendations",
    "details": {
      "model": "logistic",
      "content_ids": ["vid01", "vid02", "vid03", "vid04", "vid05"]
    }
  },
  {
    "timestamp": "2025-04-25T10:16:45Z",
    "type": "preference_updated",
    "session_id": "sess-002",
    "message": "User added 3 new preferences",
    "details": {
      "added": ["music", "comedy", "technology"],
      "removed": []
    }
  },
  {
    "timestamp": "2025-04-25T10:18:30Z",
    "type": "like_event",
    "session_id": "sess-001",
    "message": "User liked a content item",
    "details": {
      "content_id": "vid07"
    }
  },
  {
    "timestamp": "2025-04-25T10:20:05Z",
    "type": "dislike_event",
    "session_id": "sess-003",
    "message": "User disliked a content item",
    "details": {
      "content_id": "vid11"
    }
  },
  {
    "timestamp": "2025-04-25T10:22:10Z",
    "type": "model_trained",
    "session_id": "sess-001",
    "message": "Retrained logistic model with 87 samples",
    "details": {
      "model": "logistic",
      "samples": 87,
      "accuracy": "0.83"
    }
  },
  {
    "timestamp": "2025-04-25T10:25:00Z",
    "type": "recommendation_sent",
    "session_id": "sess-004",
    "message": "Sent 3 recommendations",
    "details": {
      "model": "similarity",
      "content_ids": ["vid21", "vid22", "vid23"]
    }
  }
]

function init(){
    let table = $("#logsTable")
    let body = table.find("tbody")

    console.log(table)
    console.log(body)

    for (let dp of dummy_input) {
        let ts = dp.timestamp ?? "N/A"
        let type = dp.type ?? "N/A"
        let sid = dp.session_id ?? "N/A"
        let msg = dp.message ?? "N/A"
        let details = JSON.stringify(dp.details) ?? "N/A"

        let tr = document.createElement("tr")

        const td = txt => {
            const cell = document.createElement("td");
            cell.textContent = txt;
            return cell;
        };

        tr.append(td(ts))
        tr.append(td(type))
        tr.append(td(sid))
        tr.append(td(msg))
        tr.append(td(details))

        body.append(tr)
    }

}

$(document).ready(function(){
    init()
})

