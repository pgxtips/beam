
const dummy_input = [
  {
    "session_id": "a1b2-c3",
    "created": "2025-04-24T12:30:10Z",
    "last_seen": "2025-04-24T12:59:42Z",
    "preferences": ["coding", "technology"],
    "likes":   ["Q_03FWDBZG0", "ZLOhiGZZhVs", "zltBg1bUJjI"],
    "dislikes": ["ZvXoRoXm8DU"],
    "last_recs": [
      {"id": "Q_03FWDBZG0", "score": 0.87},
      {"id": "ZLOhiGZZhVs", "score": 0.85},
      {"id": "zltBg1bUJjI", "score": 0.83},
      {"id": "QM9j_qQZDnY", "score": 0.78},
      {"id": "z7do1hhb6fE", "score": 0.76}
    ],
    "model_samples": 7,
    "last_trained": "2025-04-24T12:59:05Z"
  },
  {
    "session_id": "f4e5-d6",
    "created": "2025-04-24T12:42:03Z",
    "last_seen": "2025-04-24T12:58:11Z",
    "preferences": ["gaming"],
    "likes":   [],
    "dislikes": [],
    "last_recs": [
      {"id": "xA1BCdEFgh0", "score": 0.65},
      {"id": "7TuvWxyz123", "score": 0.63},
      {"id": "mNOPqr45STU", "score": 0.61}
    ],
    "model_samples": 2,
    "last_trained": "2025-04-24T12:42:04Z"
  },
  {
    "session_id": "8a9b-00",
    "created": "2025-04-24T11:55:44Z",
    "last_seen": "2025-04-24T12:57:22Z",
    "preferences": ["music", "lofi", "study"],
    "likes":   ["LOFIbeat001", "LOFIbeat007", "CalmTrack22"],
    "dislikes": ["HeavyMetal99", "Dubstep77"],
    "last_recs": [
      {"id": "LOFIbeat014", "score": 0.91},
      {"id": "CalmTrack25", "score": 0.88},
      {"id": "StudySound10", "score": 0.86},
      {"id": "RelaxLoop03", "score": 0.85}
    ],
    "model_samples": 12,
    "last_trained": "2025-04-24T12:56:58Z"
  }
]

function init(){
    let table = $("#sessionTable")
    let body = table.find("tbody")

    console.log(table)
    console.log(body)

    for (let dp of dummy_input) {
        let sid = dp.session_id ?? "N/A"
        let created = dp.created ?? "N/A"
        let last_seen = dp.last_seen ?? "N/A"
        let prefs = dp.preferences ?? "N/A"
        let likes = dp.likes ?? "N/A"
        let dislikes = dp.dislikes ?? "N/A"
        let last_recs = dp.dislikes ?? "N/A"
        let models_samples = dp.models_samples ?? "N/A"
        let last_trained = dp.last_trained ?? "N/A"

        let tr = document.createElement("tr")

        const td = txt => {
            const cell = document.createElement("td");
            cell.textContent = txt;
            return cell;
        };

        tr.append(td(sid))
        tr.append(td(created))
        tr.append(td(last_seen))
        tr.append(td(likes.length))
        tr.append(td(dislikes.length))
        tr.append(td(prefs.length))

        body.append(tr)
    }
}

$(document).ready(function(){
    init()
})

