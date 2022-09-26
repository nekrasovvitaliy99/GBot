from flask import Flask
from flask import request
from flask import Response

from githubresponseexception import GitHubResponseException
from userreposendpoint import UserReposEndPoint
from userreposissueendpoint import UserReposIssueEndPoint

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

@app.route('/<username>/repos', methods = ['GET'])
def repos(username):
    try:
        token = getToken()
        end_point = UserReposEndPoint(username, token)
        response = end_point.getResultResponce()
        return response
    except GitHubResponseException as e:
        return getGitHubResponseResponse(e)
    except Exception as e:
        return getExceptionResponse(e)

@app.route('/<username>/<repo>/issue', methods = ['GET', 'POST'])
def issue(username, repo):
    try:
        token = getToken()
        if request.method != 'POST':
            r = Response(response = '{"message":"You must use POST"}',
                          status = 500,
                        mimetype = 'application/json')
            return r
        title = request.json.get('title')
        body = request.json.get('body')
        end_point = UserReposIssueEndPoint(username, repo, title, body, token)
        response = end_point.getResultResponce()
        return response;
    except GitHubResponseException as e:
        return getGitHubErrorResponse(e)
    except Exception as e:
        return getExceptionResponse(e)

@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

def getGitHubResponseResponse(e):
    return Response(response = '{"message":"' + e.message + '"}',
                      status = e.status_code,
                    mimetype = 'application/json')

def getExceptionResponse(e):
    return Response(response = '{"message":"' + str(e) + '"}',
                      status = 500,
                    mimetype = 'application/json')

# Returns token
def getToken()-> str:
    file_token = open('token.txt', mode='r')
    token = file_token.read()
    return token