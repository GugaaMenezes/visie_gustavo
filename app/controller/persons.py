from app import app, db
from app.models.persons import PersonModels

from config_log import logger

from flask import request, jsonify
from sqlalchemy import delete, update
from sqlalchemy.orm import sessionmaker
import datetime

session = db.session


def person():
    
    accepter_method = ["GET", "POST"]
    
    if request.method not in accepter_method:
        return jsonify({"success": False, "message": "Method Not Allowed."}), 405, {"ContentType": "application/json"}
    
    if request.method == "GET":
        success_status, message_status, http_code = all_persons()
        
    if request.method == "POST":
        success_status, message_status, http_code = insert_person()
    
    return jsonify({"success": success_status, "message": message_status}), http_code, {"ContentType": "application/json"}

def data_person(id_pessoa):
    
    accepter_method = ["GET","PUT", "DELETE"]
    
    if request.method not in accepter_method:
        return jsonify({"success": False, "message": "Method Not Allowed."}), 405, {"ContentType": "application/json"}
    
    if request.method == "GET":
        success_status, message_status, serialized_persons, http_code = select_person(id_pessoa)
    
    if request.method == "PUT":
        success_status, message_status, http_code, serialized_persons = update_person(id_pessoa)
        
    if request.method == "DELETE":
        success_status, message_status, http_code, serialized_persons = delete_person(id_pessoa)
    
    return jsonify({"success": success_status, "message": message_status, "person": serialized_persons}), http_code, {"ContentType": "application/json"}

def all_persons():
    with app.app_context():
        try:
            persons = PersonModels.query.all()
            serialized_persons = [person.serialize() for person in persons]
            success_status = True
            http_code = 200

        except Exception as e:
            print({'Erro list_all_persons': str(e)})
            logger.error({'Erro list_all_persons': str(e)})

            success_status = False
            serialized_persons = []
            http_code = 500

        finally:
            session.close()
            return success_status, serialized_persons, http_code
        
def insert_person():
    
    data = request.json
    nome = data.get("nome")
    rg = data.get("rg")
    cpf = data.get("cpf")
    data_nascimento = data.get("data_nascimento")
    data_admissao = data.get("data_admissao")

    new_person = PersonModels(nome, rg, cpf, data_nascimento,data_admissao)
    
    with app.app_context():
        try:
            session.add(new_person)
            session.commit()
            
            success_status = True
            message_status = "Insert new person successfully"
            http_code = 200
            
        except Exception as e:
            session.rollback()
            logger.error({'Erro': str(e)})
            print({'Erro': str(e)})
            
            success_status = False
            message_status = "Erro insert person"
            http_code = 403
        finally:
            session.close()
            return success_status, message_status, http_code
        
def update_person(id_pessoa):
    
    data = request.json
    nome = data.get("nome")
    rg = data.get("rg")
    cpf = data.get("cpf")
    
    try:
        data_nascimento = datetime.datetime.strptime(data.get("data_nascimento"), "%Y-%m-%d")
    except ValueError:
        data_nascimento = datetime.datetime.strptime(data.get("data_nascimento"), "%d/%m/%Y").strftime("%Y-%m-%d")

    try:
        data_admissao = datetime.datetime.strptime(data.get("data_admissao"), "%Y-%m-%d")
    except ValueError:
        data_admissao = datetime.datetime.strptime(data.get("data_admissao"), "%d/%m/%Y").strftime("%Y-%m-%d")

    
    update_info_person = update(PersonModels).where(PersonModels.id_pessoa == id_pessoa).values(nome=nome, rg=rg, cpf=cpf, data_nascimento=data_nascimento, data_admissao=data_admissao)
    
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        try:
            success_status, message_status, serialized_persons, http_code = select_person(id_pessoa)
            
            if success_status != True:

                success_status = False
                message_status = "Person not found"
                serialized_persons = []
                http_code = 404
                return success_status, message_status, http_code
            
            session.execute(update_info_person)
            session.commit()

            success_status = True
            message_status = "Update info person successfully"
            http_code = 200
            serialized_persons = serialized_persons
            
        except Exception as e:
            session.rollback()
            logger.error({'Erro': str(e)})
            print({'Erro': str(e)})
            
            success_status = False
            message_status = "Erro update info person"
            http_code = 403
            serialized_persons = "Person not found"
            
        finally:
            session.close()
            return success_status, message_status, http_code, serialized_persons
        
def delete_person(id_pessoa):

    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        
        try:
            success_status, message_status, serialized_persons, http_code = select_person(id_pessoa)
            if success_status != True:

                success_status = False
                message_status = "Person not found"
                serialized_persons = []
                http_code = 404
                return success_status, message_status, http_code
                
        
            delete_person = delete(PersonModels).where(PersonModels.id_pessoa == id_pessoa)

            session.execute(delete_person)
            session.commit()
            
            success_status = True
            message_status = "Delete person successfully"
            http_code = 200
            serialized_persons = serialized_persons
                
        except Exception as e:
            session.rollback()
            logger.error({'Erro': str(e)})
            print({'Erro': str(e)})
            
            success_status = False
            message_status = "Erro delete person"
            http_code = 403
            serialized_persons = message_status
        finally:
            session.close()
            return success_status, message_status, http_code, serialized_persons


def select_person(id_pessoa):
    try:
        selected_person = PersonModels.query.filter_by(id_pessoa=id_pessoa).first()
        if not selected_person:
            serialized_persons = []
            success_status = False
            message_status = "Person not found"
            http_code = 404
            return success_status, message_status, http_code
            
        serialized_persons = selected_person.serialize()
        success_status = True
        message_status = "Person found"
        http_code = 200
        
    except Exception as e:
        session.rollback()
        logger.error({'Erro': str(e)})
        print({'Erro': str(e)})
        success_status = False
        serialized_persons = message_status
        message_status = "Person not found"
        http_code = 403
        
    finally:
        session.close()
        return success_status, message_status, serialized_persons, http_code