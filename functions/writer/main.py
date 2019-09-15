import flask
from google.cloud import firestore

def writeData(request):
  db = firestore.Client()
  request_json = request.get_json(silent=True)
  req_title = None
  req_status = None
  resp = None
  
  if request_json and 'title' in request_json:
    req_title = request_json['title']

  if request_json and 'status' in request_json:
    req_status = request_json['status']

  if req_title and req_status:
    doc_ref = db.collection(u'media_content').document(u'' + req_title)
    doc_ref.set({
      u'title': u'' + req_title,
      u'status': u'' + req_status
    })

    resp = flask.jsonify(
      title=req_title,
      status=req_status
    )
  else:
    resp = "Please provide title and status parameters"

  return resp
