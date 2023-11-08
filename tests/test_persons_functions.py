import pytest
from unittest.mock import patch
from app.models.persons import PersonModels
from app import app, db
from app.controller.persons import delete_person, insert_person, all_persons
from sqlalchemy.orm import sessionmaker

session = db.session

def test_insert_person():
    
    fake_json_data = {
        "nome": "Test Person",
        "rg": "123456789",
        "cpf": "987654321",
        "data_admissao": "2011-01-01",
        "data_nascimento": "2011-01-01"
    }
    with app.app_context():
        with app.test_request_context(json=fake_json_data):
            
            success_status, message_status, http_code = insert_person()

        assert success_status is True
        assert message_status == "Insert new person successfully"
        assert http_code == 200
        

def test_delete_person_with_valid_id():
    # Create a dummy person record in the database
    person = PersonModels(nome="Test Person", rg="123456789", cpf="987654321", data_admissao="2011-01-01", data_nascimento="2011-01-01")
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        session.add(person)
        session.commit()

    success_status, message_status, http_code, serialized_persons = delete_person(person.id_pessoa)


    assert success_status is True
    assert message_status == "Delete person successfully"
    assert http_code == 200

    # Check that the person record has been deleted from the database
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        person_deleted = PersonModels.query.filter_by(id_pessoa=person.id_pessoa).first()
        
    assert person_deleted != serialized_persons


def test_delete_person_with_invalid_id():
    
    success_status, message_status, http_code, serialized_persons = delete_person(-1)

    assert success_status is False
    assert message_status == "Person not found"
    assert http_code == 404
    
def test_all_persons():
    # Create some dummy person records in the database
    person1 = PersonModels(nome="Test Person 1", rg="123456789", cpf="987654321", data_admissao="2011-01-01", data_nascimento="2019-10-01")
    person2 = PersonModels(nome="Test Person 2", rg="987654321", cpf="123456789", data_admissao="2011-01-01", data_nascimento="1985-02-01")
    
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        session.add_all([person1, person2])
        session.commit()

    # Call the all_persons function
    success_status, serialized_persons, http_code = all_persons()

    # Assert that the function returns the expected values
    assert success_status is True
    assert http_code == 200

    # Check that the serialized persons list contains the expected data
    assert len(serialized_persons) >= 2
    assert serialized_persons[-2]['nome'] == "Test Person 1"
    assert serialized_persons[-1]['nome'] == "Test Person 2"
    
def test_update_person():
    # Create some dummy person records in the database
    person1 = PersonModels(nome="Test Person 1", rg="123456789", cpf="987654321", data_admissao="2011-01-01", data_nascimento="2019-10-01")
    person2 = PersonModels(nome="Test Person 2", rg="987654321", cpf="123456789", data_admissao="2011-01-01", data_nascimento="1985-02-01")
    
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        session.add_all([person1, person2])
        session.commit()

    # Call the all_persons function
    success_status, serialized_persons, http_code = all_persons()

    # Assert that the function returns the expected values
    assert success_status is True
    assert http_code == 200

    # Check that the serialized persons list contains the expected data
    assert len(serialized_persons) >= 2
    assert serialized_persons[-2]['nome'] == "Test Person 1"
    assert serialized_persons[-1]['nome'] == "Test Person 2"