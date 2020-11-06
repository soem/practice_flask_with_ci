from table_users import *

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@127.0.0.1/postgres', echo=True)

Base.metadata.create_all(engine)
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='ed', job_title='tester')
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

ed_user_comm = CommunicateInformation(email='a@a.a', mobile='0900000000',user_id=ed_user.id)
session.add(ed_user_comm)

our_user_comm = session.query(CommunicateInformation).\
                            join(CommunicateInformation.user).\
                            filter(User.name=='ed').first()
print(our_user_comm)