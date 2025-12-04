import json
from typing import Dict,Any,List,Optional
from datetime import datetime

DATA_FILE="patients.json"

class MedicalRecord:
    def __init__(self,diagnoses:Optional[List[str]]=None,medications:Optional[List[str]]=None):
        self.diagnoses=diagnoses or[]
        self.medications=medications or []
        self.history: List[Dict[str,Any]]=[]

    def add_diagnosis(self,diagnosis:str,doctor:str)->None:
        self.diagnoses.append(diagnosis)
        event={"time": datetime.now().isoformat(),"doctor":doctor,"action":"add_diagnosis","text":diagnosis}
        self.history.append(event)
    
    def add_medication(self,med:str,doctor:str)->None:
        self.medications.append(med)
        event={"time":datetime.now().isoformat(),"doctor":doctor,"action":"add_medication","text":med}
        self.history.append(event)
    
    def to_dict(self)->Dict[str,Any]:
        return{
            "diagnoses":list(self.diagnoses),
            "medications":list(self.medications),
            "history":list(self.history),

        }
    @staticmethod
    def from_dict(d:Dict[str,Any])-> "MedicalRecord":
        mr=MedicalRecord(d.get("diagnoses",[]),d.get("medications",[]))
        mr.history=d.get("history",[])
        return mr
    
class Patient:
     def __init__(self,patient_id:int,name:str,age:int,contact:str,record:Optional[MedicalRecord]=None):
        self.patient_id=int(patient_id)
        self.name=name
        self.age=int(age)
        self.contact=contact
        self.record=record or MedicalRecord()
        self.base_charge=0.0
    
     def update_diagnosis(self,medication:str,doctor:str)->None:
         self.record.add_medication(medication,doctor)
    
     def update_medication(self,medication:str,doctor:str)->None:
         self.record.add_medication(medication,doctor)
    
     def calculate_bill(self,services_cost:float,apply_senior_discount:bool=True)->float:
         total=float(self.base_charge)+float(services_cost)

         if apply_senior_discount:
             if self.age>60:
                 discount_pct=15.0
                 total=total*(1-discount_pct/100.0)
             else:
                 if self.age>=18:
                     pass
                 else:
                     pass
         return round(total,2)
     def to_dict(self)->Dict[str,Any]:
         return{
             "patient_id":self.patient_id,
             "name":self.name,
             "age":self.age,
             "contact":self.contact,
             "base_charge":self.base_charge,
             "record":self.record.to_dict(),
         }
     @staticmethod
     def from_dict(d:Dict[str,Any])->"Patient":
         rec=MedicalRecord.from_dict(d.get("record",{}))
         p=Patient(d["patient_id"],d["name"],d["age"],d.get("contact",""),rec)
         p.base_charge=d.get("base_charge",0.0)
         return p

class HospitalSystem:
    def __init__(self,data_file:str=DATA_FILE):
        self.data_file=data_file
        self.patients:Dict[int, Patient]={}
        self._load()
    
    def register_patient(self,name:str,age:int,contact:str)->Patient:
        new_id=max(self.patients.keys(),default=0)+1
        patient=Patient(new_id,name,age,contact)
        self.patients[new_id]=patient
        self._save()
        return patient
    
    def find_patient(self,patient_id:int)->Optional[Patient]:
        return self.patients.get(int(patient_id))
    
    def update_diagnosis(self,patient_id:int,diagnosis:str,doctor:str)->bool:
        p=self.find_patient(patient_id)
        if not p:
            return False
        p.update_diagnosis(diagnosis,doctor)
        self._save()
        return True
    
    def update_medication(self,patient_id:int,medication:str,doctor:str)->bool:
        p=self.find_patient(patient_id)
        if not p:
            return False
        p.update_medication(medication,doctor)
        self._save()
        return True
    
    def generate_bill(self,patient_id:int,services_cost:float)->Optional[Dict[str,Any]]:
        p=self.find_patient(patient_id)
        if not p:
            return None
        total=p.calculate_bill(services_cost)
        bill={"patient_id":p.patient_id,"name":p.name,"services_cost":services_cost,"total_due":total}
        return bill
    
    def list_patients(self)->List[Dict[str,Any]]:
        return [p.to_dict() for p in self.patients.values()]
    
    def _save(self)->None:
        data=[p.to_dict() for p in self.patients.values()]
        with open(self.data_file,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=2)
    
    def _load(self)->None:
        try:
            with open(self.data_file,"r",encoding="utf-8") as f:
                data=json.load(f)
            for entry in data:
                p=Patient.from_dict(entry)
                self.patients[p.patient_id]=p
        except FileNotFoundError:
            self.patients={}
    

def demo():
    hospital=HospitalSystem()
    p1=hospital.register_patient("Asha Rai",65,"1450000")
    p2=hospital.register_patient("Bikram Thapa",45,"98111111")

    print("Registered patients:")
    for p in hospital.list_patients():
        print(p["patient_id"],p["name"],"age:",p["age"])
    
    hospital.update_diagnosis(p1.patient_id,"Hypertension",doctor="Dr.Sharma")
    hospital.update_medication(p1.patient_id,"Amlodipine 5mg",doctor="Dr.Sharma")

    bill1=hospital.generate_bill(p1.patient_id,services_cost=2000.0)
    bill2=hospital.generate_bill(p2.patient_id,services_cost=2000.0)

    print("\nBills:")
    print(bill1)
    print(bill2)

    print("\nMedical record for Asha (diagnoses):",hospital.find_patient(p1.patient_id).record.diagnoses)
    print("History entries (Asha):",hospital.find_patient(p1.patient_id).record.history)

if __name__=="__main__":
    demo()







