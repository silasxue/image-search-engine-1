import json



for k, v in d.iteritems():
	print json.dumps(v, indent=4, sort_keys=True)