import socket
import connections
import responses
import memegenerator

page = connections.edit_response(responses.homepage, "memer", memegenerator.random_meme())
#print(connections.readresponse(responses.homepage))

conn, adrr, request = connections.hostconn("0.0.0.0", 10000)
connections.respond(conn, page)
