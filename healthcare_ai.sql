-- 1️⃣ Create Database
CREATE DATABASE IF NOT EXISTS healthcare_ai;
USE healthcare_ai;

-- 2️⃣ Patients Table
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3️⃣ Patient Records Table
CREATE TABLE IF NOT EXISTS patient_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    disease VARCHAR(50),
    input_data JSON,
    result VARCHAR(50),
    probability FLOAT,
    image_path VARCHAR(255),            -- optional: OpenCV / image file path
    notes VARCHAR(255),                 -- optional: doctor / assistant remarks
    is_active BOOLEAN DEFAULT TRUE,     -- optional: soft delete
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- 4️⃣ Index for faster queries
CREATE INDEX idx_patient_id ON patient_records(patient_id);
