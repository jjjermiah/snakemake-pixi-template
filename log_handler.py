import json

def job_to_dict(msg):
    """Given a message dictionary, we want to loop through the key, value
    pairs and convert some attributes to strings (e.g., jobs are fine to be
    represented as names) and return a dictionary.
    """
    result = {}
    for key, value in msg.items():
        # For a job, the name is sufficient
        if key == "job":
            result[key] = str(value)

        # For an exception, return the name and a message
        elif key == "exception":
            result[key] = "{}: {}".format(
                msg["exception"].__class__.__name__,
                msg["exception"] or "Exception",
            )

        # All other fields are json serializable
        else:
            result[key] = value

    # Return a json dumped string
    return json.dumps(result)
    
def log_handler(msg: dict):
    with open("log.json", "a") as f:
        f.write(job_to_dict(msg) + "\n")