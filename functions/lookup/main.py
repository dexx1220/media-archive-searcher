import flask
from google.cloud import firestore

def lookup(request):
  db = firestore.Client()
  request_args = request.args
  resp = None

  if request_args and 'title' in request_args:
    doc_ref = db.collection(u'media_content').document(u'' + request_args['title'])
    try:
      doc = doc_ref.get()
      payload = doc.to_dict()
      resp = flask.jsonify(
        title=payload['title'],
        status=payload['status']
      )
    except:
      resp = 'No data found'
  else:
    resp = 'Please provide title parameter'

  return resp
