from dao.hospitalserviceimpl import HospitalServiceImpl
from entity.appointment import Appointment
from myexceptions.patient_exceptions import PatientNumberNotFoundException

def main():
    try:
        # Instantiate the HospitalServiceImpl class
        hospital_service = HospitalServiceImpl()

        # Trigger various methods
        appointment_id = 1
        appointment = hospital_service.getAppointmentById(appointment_id)
        print("Appointment by ID:", appointment)

        patient_id = "P001"
        appointments_for_patient = hospital_service.getAppointmentsForPatient(patient_id)
        print(f"Appointments for Patient {patient_id}:")
        for appt in appointments_for_patient:
            print(appt)

        doctor_id = "D001"
        appointments_for_doctor = hospital_service.getAppointmentsForDoctor(doctor_id)
        print(f"Appointments for Doctor {doctor_id}:")
        for appt in appointments_for_doctor:
            print(appt)

        # Create a new appointment
        new_appointment = Appointment(appointmentId=3, patientId="P002", doctorId="D002",
                                      appointmentDate="2023-01-01", description="New Appointment")
        success = hospital_service.scheduleAppointment(new_appointment)
        print("Appointment Scheduled:", success)

        # Update an existing appointment
        existing_appointment = Appointment(appointmentId=1, patientId="P001", doctorId="D001",
                                           appointmentDate="2023-01-02", description="Updated Appointment")
        success = hospital_service.updateAppointment(existing_appointment)
        print("Appointment Updated:", success)

        # Cancel an appointment
        appointment_to_cancel = 3
        
        success = hospital_service.cancelAppointment(appointment_to_cancel)
        print("Appointment Canceled:", success)

        # Test handling PatientNumberNotFoundException
        invalid_patient_id = 4
        appointments_for_invalid_patient = hospital_service.getAppointmentsForPatient(invalid_patient_id)
        print(f"Appointments for Invalid Patient {invalid_patient_id}:", appointments_for_invalid_patient)

    except PatientNumberNotFoundException as e:
        print(f"Caught PatientNumberNotFoundException: {e}")
    except Exception as e:
        print(f"Unexpected exception: {e}")

if __name__ == "__main__":
    main()
