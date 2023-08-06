import collections
import os
import json
import ast
import string
import random
import copy
from json import JSONDecodeError
from os import path


class Database:
    db = None
    db_path = None
    db_collection = None
    db_default_path = 'jlod/databases'
    db_dictionary = None
    DBManager = None

    def __init__(self, db_path=db_default_path, dbi=db, collection=db_collection):
        if db_path.__eq__(self.db_default_path):
            self.db_path = self.db_default_path
        else:
            self.db_path = db_path
        self.db = dbi
        self.db_collection = collection
        self.DBManager = DatabaseManager(self.db_collection)
        self.db_dictionary = {
            "documents": [
            ]
        }

    @property
    def instance(self):
        return Database(self.db_path, self.db)

    def connect(self, db_name=None):
        db_connection = False
        if not str(db_name).endswith('.db'):
            self.db = self.db_path + '/' + db_name + '.db'

        try:
            if db_name is not None:
                if not os.path.exists(self.db):
                    os.makedirs(self.db)
                    console.log('Database [' + db_name + '] created at [' + self.db_path + ']')
                    db_connection = True
                else:
                    db_connection = True
            else:
                db_connection = False
                console.log('Oops! Unable to find database ' + db_name)

        except FileNotFoundError and OSError:
            console.log('Oops! Unable to initialize local database ' + db_name + ' at ' + self.db_path)
            return db_connection
        else:
            return Database(self.db_path, self.db)

    def collection(self, collection_name=""):
        if collection_name is not None:

            if not collection_name.endswith('.collection'):
                collection_name = collection_name + '.collection'

            col = self.db + '/' + collection_name
            self.db_collection = col
            open(col, 'a+')  # create collection

            if path.exists(col):
                return Database(self.db_path, self.db, col)
            else:
                console.log('Unable to create collection' + collection_name)
                return None
        else:
            print('Oops! No collection provided')

    def exportTo(self, mongo_collection: classmethod, conditions={}):
        self.DBManager = DatabaseManager(self.db_collection)
        try:
            import pymongo
            documents: dict
            if conditions.__len__() > 0:
                documents = self.DBManager.search(conditions)
            else:
                documents = self.DBManager.read()
            mongo_collection.insert_many(documents)
        except ImportError:
            console.log('Oops! Unable to find MangoDB')
            return False
        else:
            return True

    def importFrom(self, mongo_collection: classmethod, conditions: dict):
        self.DBManager = DatabaseManager(self.db_collection)
        doc: dict
        try:
            import pymongo
            documents: dict
            if conditions.__len__() > 0:
                documents = mongo_collection.find({}, conditions)
            else:
                documents = mongo_collection.find({}, conditions)
            for doc in documents:

                if '_id' in doc.keys():
                    doc.pop('_id')
                if 'id' in doc.keys():
                    doc.pop('id')
                if doc.__len__() > 0:
                    self.add(doc)
        except ImportError as error:
            console.log('Oop! Unable to find MangoDB')
            return [error]
        else:
            return self.DBManager.read()

    def override(self, obj: dict):
        document: dict
        if dict is not None:
            documentId = self.DBManager.generateId()
            obj.__setitem__('id', documentId)
            dictionary = self.db_dictionary.get('documents')
            dictionary.append(obj)
            self.DBManager.write(self.db_dictionary)
            return True
        else:
            print('No data found!')
            return False

    def add(self, obj: dict):
        document: dict
        if dict is not None:

            if os.path.getsize(self.db_collection) == 0:
                self.override(obj)
            else:
                document = self.DBManager.read()
                documentId = self.DBManager.generateId()
                obj.__setitem__('id', documentId)
                document.append(obj)
                dictionary = {
                    'documents': document
                }
                self.DBManager.write(dictionary)
            return True
        else:
            return False

    def addMany(self, documents: []):
        try:
            if documents.__len__() > 0:
                for document in documents:
                    self.add(document)
            console.log(str(len(documents)) + ' documents added')
        except ValueError as ex:
            return False
        else:
            return True

    @property
    def documents(self):
        document: dict
        document = self.DBManager.read()
        return document

    @property
    def count(self):
        document: dict
        document = self.DBManager.read()
        return document.__len__()

    @property
    def truncate(self):
        self.DBManager.truncate()
        return True

    @property
    def drop(self):
        try:
            os.remove(self.db_collection)
        except FileNotFoundError:
            print("Collection " + self.db_collection + "  not found ")
        else:
            return True

    @property
    def size(self):
        self.DBManager = DatabaseManager(self.db_collection)
        return self.DBManager.getSize()

    def update(self, keyAndReplacement: dict, conditions=None):
        if conditions is None:
            document = self.DBManager.read()
        else:
            document = self.DBManager.search(conditions)

        self.DBManager.update(document, keyAndReplacement)

    def removeAll(self):
        self.DBManager.truncate()

    def sort(self, sorts=None, conditions=None, limit=0):
        self.DBManager = DatabaseManager(self.db_collection)
        if conditions is None and sorts is None:
            documents = self.DBManager.read()
        else:
            if conditions is not None and conditions.__len__() > 0:
                documents = self.DBManager.search(conditions)
            else:
                documents = self.DBManager.read()

            if limit > 0:
                documents = self.distinct(documents, limit)
            else:
                if conditions:
                    documents = self.DBManager.search(conditions)

            if sorts.__len__() > 0:
                for key, val in sorts.items():
                    keyName = key
                    if val.__eq__(-1):
                        reverseFlag = False
                    else:
                        reverseFlag = True
                    documents.sort(key=lambda x: x.__getitem__(
                        keyName), reverse=reverseFlag)
        return documents

    def remove(self, conditions=None):
        if conditions is None:
            document = self.DBManager.read()
        else:
            document = self.DBManager.search(conditions)

        if conditions is None:
            return self.truncate
        else:
            return self.DBManager.remove(document)

    def getOne(self, keyList=None, conditions=None):
        resultSet = []
        if conditions is None:
            documents = self.DBManager.read()
        else:
            documents = self.DBManager.search(conditions)

        if documents.__len__() > 0:
            resultSet.append(documents[0])

        return self.DBManager.get(resultSet, keyList)

    def get(self, keyList=None, conditions=None):
        if conditions is None:
            document = self.DBManager.read()
        else:
            document = self.DBManager.search(conditions)

        return self.DBManager.get(document, keyList)

    def findOne(self, conditions=None):
        self.DBManager = DatabaseManager(self.db_collection)
        resultSet = []
        if conditions is not None:
            documents = self.DBManager.search(conditions)
        else:
            documents = self.DBManager.read()

        if documents.__len__() > 0:
            resultSet.append(documents[0])
        return resultSet

    def distinct(self, conditions=None, limit=0):
        keylookup = ""
        resultSet = []
        key_checker = {}
        already_added = []

        if isinstance(conditions, dict):
            for key, vlaue in conditions.items():
                valuelookup = vlaue
                keylookup = key
        else:
            valuelookup = keylookup = conditions

        if conditions is not None and conditions.__len__() > 0:
            document = self.DBManager.read()
            for doc in document:
                params = doc[keylookup]
                name = doc[keylookup]
                doc_val = doc[keylookup]
                if params in key_checker:
                    key_checker[params] = doc_val
                elif name not in key_checker:
                    key_checker[params] = doc_val
            for doc in document:
                name = doc[keylookup]
                doc_val = doc[keylookup]
                if (key_checker[name] == doc_val) and (name not in already_added):
                    resultSet.append(doc)
                    already_added.append(name)
        if limit > 0:
            resultSet = distinct(resultSet, limit)
        return resultSet

    def find(self, conditions=None, limit=0):
        self.DBManager = DatabaseManager(self.db_collection)
        if conditions is None and limit == 0:
            documents = self.DBManager.read()
            return documents
        else:
            if conditions is not None and conditions.__len__() > 0:
                documents = self.DBManager.search(conditions)
            else:
                documents = self.DBManager.read()
            if limit > 0:

                return documents
            else:
                if conditions:
                    return self.DBManager.search(conditions)
                else:
                    return documents


class DatabaseManager:
    db_collection = None

    def __init__(self, collection=db_collection):
        self.db_collection = collection

    def generateId(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

    def getSize(self):
        st = os.stat(self.db_collection)
        return st.st_size

    def truncate(self):
        collection = open(self.db_collection, 'r+')
        collection.truncate()
        collection.close()

    def write(self, document: dict):
        collectionWriter = open(self.db_collection, 'w')
        collectionWriter.write(str(document))
        collectionWriter.close()

    def read(self):
        try:
            collectionReader = open(self.db_collection, 'r')
            document = collectionReader.read()
            if document.__ne__(''):
                document = document.replace("'", "\"")
                document = json.loads(document)
            else:
                document = {
                    "documents": [
                    ]
                }
        except JSONDecodeError as error:
            return [error]
        else:
            return document.get('documents')

    def get(self, document: dict, keys=None):

        resultSet = []
        if keys is not None:
            if keys.__ne__("*"):
                for doc in document:
                    localDict = {
                        "$~": "init"
                    }
                    for key in keys:
                        if key in doc.keys():
                            if type(doc[key]) is string:
                                localDict.update({'' + key + '': '' + doc[key] + ''})
                            else:
                                localDict.update({'' + key + '':doc[key]})
                    localDict.pop("$~")
                    resultSet.append(localDict)
            else:
                resultSet = document
            return resultSet
        else:
            return document

    def extract(self, doc: dict, key: str, operator: str, value):
        resultSet = None
        if operator.__eq__("$eq"):
            if str(doc[key]).lower() == str(value).lower():
                resultSet = doc
        elif operator.__eq__("$ne"):
            if str(doc[key]).lower() != str(value).lower():
                resultSet = doc
        elif operator.__eq__("$gt"):
            if int(str(doc[key]).lower()) > int(str(value).lower()):
                resultSet = doc
        elif operator.__eq__("$gte"):
            if int(str(doc[key]).lower()) >= int(str(value).lower()):
                resultSet = doc
        elif operator.__eq__("$lt"):
            if int(str(doc[key]).lower()) < int(str(value).lower()):
                resultSet = doc
        elif operator.__eq__("$lte"):
            if int(str(doc[key]).lower()) <= int(str(value).lower()):
                resultSet = doc
        elif operator.__eq__("$in"):
            if str(doc[key]).lower() == str(value).lower():
                resultSet = doc

        elif operator.__eq__("$nin"):
            if str(doc[key]).lower() != str(value).lower():
                resultSet = doc

        return resultSet

    def query(self, documents: dict, logicKey: str, conditions: dict):
        resultSet = []
        if type(conditions) is not dict and isinstance(conditions, collections.Sequence):
            if logicKey.__eq__("$or"):
                for cond in conditions:
                    for citems in cond.items():
                        key = citems[0]
                        items = citems[1]

                        for citems in items.items():
                            operator = citems[0]
                            value = citems[1]
                            for doc in documents:
                                if key in doc:
                                    result = self.extract(doc, key, operator, value)
                                    if result is not None:
                                        resultSet.append(result)
            elif logicKey.__eq__("$and"):
                for doc in documents:
                    query = []
                    for cond in conditions:
                        for citems in cond.items():
                            key = citems[0]
                            items = citems[1]
                            for citems in items.items():
                                operator = citems[0]
                                value = citems[1]

                                if key in doc:
                                    result = self.extract(doc, key, operator, value)
                                    if result is not None:
                                        query.append(1)

                    if query.__len__() == conditions.__len__():
                        if doc not in resultSet:
                            resultSet.append(doc)
        else:
            for cond in conditions.items():
                key = str(cond[0])
                items = cond[1].items()
                for citems in items:
                    operator = citems[0]
                    value = citems[1]
                    for doc in documents:
                        if key in doc:
                            result = self.extract(doc, key, operator, value)
                            if result is not None:
                                resultSet.append(result)
        return resultSet

    def search(self, conditions: dict):
        documents = self.read()
        resultSet = []

        if type(conditions) is list:
            for condition in conditions:
                for cond in condition.items():
                    key = str(cond[0]).lower()
                    items = cond[1]
                    for citems in items.items():
                        operator = citems[0]
                        value = citems[1]
                        for doc in documents:
                            result = self.extract(doc, key, operator, value)
                            if result is not None:
                                if result not in resultSet:
                                    resultSet.append(result)

        elif type(conditions) is dict:
            for cond in conditions.items():
                key = str(cond[0]).lower()
                value = cond[1]

                if key.startswith("$"):
                    if type(value) is list:
                        for cdoc in value:
                            for condoc in cdoc.items():
                                key = str(condoc[0]).lower()
                                items = condoc[1]
                                for citems in items.items():
                                    operator = citems[0]
                                    value = citems[1]
                                    for doc in documents:
                                        result = self.extract(doc, key, operator, value)
                                        if result is not None:
                                            if result not in resultSet:
                                                resultSet.append(result)
                    else:
                        if self.query(documents, key, value).__len__() > 0:
                            resultSet = self.query(documents, key, value)[:]
                else:

                    if type(value) is dict:
                        for citems in value.items():
                            operator = citems[0]
                            value = citems[1]
                            for doc in documents:
                                if type(value) is not str and isinstance(value, collections.Sequence):
                                    for each in value:
                                        result = self.extract(doc, key, operator, each)
                                        if result is not None:
                                            if str(operator) == "$nin":
                                                if result not in resultSet:
                                                    if result[key] not in value:
                                                        lowerResult = map(str, value)
                                                        lowerResult = map(str.lower, lowerResult)
                                                        if str(result[key]).lower() not in lowerResult:
                                                            resultSet.append(result)
                                            else:
                                                if result not in resultSet:
                                                    resultSet.append(result)
                                else:
                                    result = self.extract(doc, key, operator, value)
                                    if result is not None:
                                        if result not in resultSet:
                                            resultSet.append(result)

                    else:
                        for doc in documents:
                            for cond in conditions.items():
                                key = str(cond[0])
                                value = str(cond[1])
                                if str(value).__contains__('[') and str(value).__contains__(']'):
                                    values = ast.literal_eval(value)
                                    for val in values:
                                        if key in doc:
                                            if str(doc[key]).lower() == str(val).lower():
                                                if doc not in resultSet:
                                                    resultSet.append(doc)
                                else:
                                    if str(doc[key]).lower() == str(value).lower():
                                        if doc not in resultSet:
                                            resultSet.append(doc)
        return resultSet

    def update(self, document: dict, keyAndReplacement: dict):
        if keyAndReplacement.__len__() > 0 and document.__len__() > 0:
            oldDocument = copy.deepcopy(document)
            for doc in document:
                for sar in keyAndReplacement.items():
                    key = sar[0]
                    value = sar[1]
                    if key in doc:
                        doc[key] = value
                    else:
                        doc.__setitem__(key, value)

            base = self.read()
            for oldDoc in oldDocument:
                base = [x for x in base if x != oldDoc]

            for newDoc in document:
                if newDoc is not None:
                    base.append(newDoc)

            dictionary = {
                'documents': base
            }
            self.write(dictionary)
            return True
        else:
            return False

    def remove(self, document: dict):

        base = self.read()
        for doc in document:
            base = [x for x in base if x != doc]

        dictionary = {
            'documents': base
        }
        self.write(dictionary)
        return True


class Console:
    def log(self, msg):
        print(msg)


console = Console()
database = Database()
