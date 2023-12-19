import datetime
import time

class Application:
    def __init__(self, id, company_name, position, date_of_apply, side, status, cv_version, mode, contract_type, job_type):
        self.id = id
        self.company_name = company_name
        self.position = position
        self.date_of_apply = date_of_apply
        self.side = side
        self.status = status
        self.cv_version = cv_version
        self.mode = mode
        self.contract_type = contract_type
        self.job_type = job_type

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def date_of_apply(self):
        return self._date_of_apply

    @date_of_apply.setter
    def date_of_apply(self, value):
        self._date_of_apply = value

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def cv_version(self):
        return self._cv_version

    @cv_version.setter
    def cv_version(self, value):
        self._cv_version = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value

    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value

    def current_day(self):
        date = datetime.date.today()
        return date
        
    def count_days_from_application(self):
        apply_day = datetime.datetime.strptime(self.date_of_apply, '%Y-%m-%d').date()
        current_day = self.current_day()
        result = abs((current_day - apply_day).days)
        return result

app = Application(1, "Company X", "Developer", "2023-12-22", "Internal", "Pending", "v1", "Full-time", "Permanent", "IT")
print(app.count_days_from_application())