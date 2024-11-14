// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDB {

    struct Student {
        string name;
        uint256 roll_no;
        string class;
    }

    Student[] private students;

    // Add a new student
    function addStudent(string memory name, uint256 roll_no, string memory class) public {
        students.push(Student(name, roll_no, class));
    }

    // Get a student's information by their ID
    function getStudentById(uint256 id) public view returns(string memory, uint256, string memory) {
        require(id < students.length, "Student does not exist in database");
        return (students[id].name, students[id].roll_no, students[id].class);
    }

    // Get the total number of students
    function getTotalNumberOfStudents() public view returns(uint256) {
        return students.length;
    }

    // Update a student's information by their ID
    function updateStudent(uint256 id, string memory name, uint256 roll_no, string memory class) public {
        require(id < students.length, "Student does not exist in database");
        students[id] = Student(name, roll_no, class);
    }

    // Delete a student from the database by their ID
    function deleteStudent(uint256 id) public {
        require(id < students.length, "Student does not exist in database");

        // Move the last student in the array to the deleted position to avoid gaps
        students[id] = students[students.length - 1];
        students.pop(); // Remove the last student
    }
}
