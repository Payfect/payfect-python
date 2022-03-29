import payfect


class APIResource():
    @classmethod
    def class_url(cls):
        return f'{payfect.api_base}/{cls.OBJECT_NAME}s/'
