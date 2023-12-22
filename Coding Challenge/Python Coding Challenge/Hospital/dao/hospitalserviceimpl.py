import mysql.connector
from dao.ihospitalservice import IHospitalService
from entity.appointment import Appointment
from util.dbconnection import DBConnection
from myexceptions.patient_exceptions import PatientNumberNotFoundException
from typing import List

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def getAppointmentById(self, appointmentId) -> Appointment:
        self.cursor.execute("SELECT * FROM appointments WHERE appointmentId=%s", (appointmentId,))
        result = self.cursor.fetchone()
        if result:
            appointment = Appointment(*result)
            return appointment
        return None

    # def getAppointmentsForPatient(self, patientId) -> List[Appointment]:
    #     self.cursor.execute("SELECT * FROM appointments WHERE patientId=%s", (patientId,))
    #     results = self.cursor.fetchall()
    #     appointments = [Appointment(*row) for row in results]
    #     return appointments
    def getAppointmentsForPatient(self, patientId) -> List[Appointment]:
        try:
            self.cursor.execute("SELECT * FROM appointments WHERE patientId=%s", (patientId,))
            results = self.cursor.fetchall()
            if not results:
                raise PatientNumberNotFoundException(patientId)
            
            appointments = [Appointment(*row) for row in results]
            return appointments
        except PatientNumberNotFoundException as e:
            # Log or handle the exception as needed
            print(f"Exception: {e}")
            return []
        except Exception as e:
            # Log or handle other exceptions
            print(f"Unexpected exception: {e}")
            return []

    def getAppointmentsForDoctor(self, doctorId) -> List[Appointment]:
        self.cursor.execute("SELECT * FROM appointments WHERE doctorId=%s", (doctorId,))
        results = self.cursor.fetchall()
        appointments = [Appointment(*row) for row in results]
        return appointments

    def scheduleAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                INSERT INTO appointments (appointmentId, patientId, doctorId, appointmentDate, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (appointment.getAppointmentId(), appointment.getPatientId(),
                  appointment.getDoctorId(), appointment.getAppointmentDate(),
                  appointment.getDescription()))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error scheduling appointment: {e}")
            return False

    def updateAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                UPDATE appointments
                SET patientId=%s, doctorId=%s, appointmentDate=%s, description=%s
                WHERE appointmentId=%s
            """, (appointment.getPatientId(), appointment.getDoctorId(),
                  appointment.getAppointmentDate(), appointment.getDescription(),
                  appointment.getAppointmentId()))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error updating appointment: {e}")
            return False

    def cancelAppointment(self, appointmentId) -> bool:
        try:
            self.cursor.execute("DELETE FROM appointments WHERE appointmentId=%s", (appointmentId,))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error canceling appointment: {e}")
            return False
