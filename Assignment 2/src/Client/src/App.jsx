import React, { useState, useEffect } from "react";
import axios from "axios";
import Swal from "sweetalert2";
import Task_card from "./Components/Task_card";
import Task_Form from "./Components/Task_Form";
import Task_Edit from "./Components/Task_Edit";
const App = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({
        title: "",
        due_date: "",
        type: "personal",
        priority: "low",
        description: "",
    });
    const [editTask, setEditTask] = useState(null);
    useEffect(() => {
        console.log("Tasks:", tasks);
    }, [tasks]);
    // Fetch all tasks
    const mapTasks = (data) => {
        return data.map((task) => ({
            id: task[0],
            type: task[1],
            title: task[2],
            due_date: task[3],
            description: task[4],
            priority: task[5],
            status: task[6],
        }));
    };
    const fetchTasks = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:5000/tasks");
            setTasks(mapTasks(response.data)); // Map server response
        } catch (error) {
            console.error("Error fetching tasks:", error);
        }
    };

    // Handle input change
    const handleChange = (e) => {
        setNewTask({ ...newTask, [e.target.name]: e.target.value });
    };

    // Create a new task
    const createTask = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://127.0.0.1:5000/tasks", newTask);
            fetchTasks();
            setNewTask({
                title: "",
                due_date: "",
                type: "personal",
                priority: "low",
                description: "",
            });
            Swal.fire("Success", "Task created successfully", "success");
        } catch (error) {
            Swal.fire({
                icon: "error",
                title: "Error creating task",
                text: "Something went wrong!",
            });
            console.error("Error creating task:", error);
        }
    };

    // Update a task
    const updateTask = async (e) => {
        e.preventDefault();
        try {
            await axios.put(
                `http://127.0.0.1:5000/tasks/${editTask.id}`,
                editTask
            );
            fetchTasks();
            setEditTask(null);
            Swal.fire("Success", "Task updated successfully", "success");
        } catch (error) {
            Swal.fire({
                icon: "error",
                title: "Error updating task",
                text: "Something went wrong!",
            });
            console.error("Error updating task:", error);
        }
    };

    // Delete a task
    const deleteTask = async (id) => {
        try {
            await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
            fetchTasks();
            Swal.fire("Success", "Task deleted successfully", "success");
        } catch (error) {
            Swal.fire({
                icon: "error",
                title: "Error deleting task",
                text: "Something went wrong!",
            });
            console.error("Error deleting task:", error);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div className="min-h-screen bg-gray-100 p-6">
            <div className="max-w-4xl mx-auto bg-white p-6 shadow-md rounded-lg">
                <h1 className="text-2xl font-bold text-center mb-6 text-gray-800">
                    Task Manager
                </h1>

                {/* Create Task Form */}
                <Task_Form
                    newTask={newTask}
                    handleChange={handleChange}
                    createTask={createTask}
                />
                {/* Task List */}
                <div className="mt-8 relative w-full">
                    <hr />
                    <h2 className="pt-6 text-xl font-semibold text-gray-800">
                        Tasks
                    </h2>
                    {editTask && (
                        <Task_Edit
                            editTask={editTask}
                            setEditTask={setEditTask}
                            updateTask={updateTask}
                        />
                    )}
                    <ul className="mt-4 space-y-4">
                        {tasks.map((task) => (
                            <Task_card
                                key={task.id}
                                task={task}
                                setEditTask={setEditTask}
                                deleteTask={deleteTask}
                            />
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default App;
