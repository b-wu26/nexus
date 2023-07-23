from . import db


class class_profile(db.Model):
    idclass_profile = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False)
    course_code = db.Column(db.String(50))
    faclty = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<class_profile {self.course_code}>"

    def __init__(self, idclass_profile, class_name, course_code, faclty):
        self.idclass_profile = idclass_profile
        self.class_name = class_name
        self.course_code = course_code
        self.faclty = faclty
