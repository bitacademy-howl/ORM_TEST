import simple_connection1 as sc
from ORM_with_SQLAlchemy.app import TravelEvent, User
from simple_connection_with_OOP import CRUD

if __name__ == "__main__":

    def search_events_by_userid(user_id):
        # user_id 를 기준으로 event 찾기, all 로 찾음
        return TravelEvent.query.filter_by(user_id=user_id).all()

    def search_event_by_eventid(event_id):
        # event_id 를 기준으로 event 를 찾기. 한개만 리턴
        return TravelEvent.query.filter_by(event_id=event_id).first()

    search_events_by_userid(0)

    TravelEvent.query.order_by(TravelEvent.created.desc()).first()
