from dbConnector.models import *

class Services:

    def get_class(c_type):
        match c_type:
            case "rubric":
                return Rubric
            case "mentor_text":
                return MentorText
            case "prompt":
                return Prompt
            case "metric":
                return Metric
            case "skill":
                return Skill
    