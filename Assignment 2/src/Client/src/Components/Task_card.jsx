import React from "react";

function Task_card({ task, setEditTask, deleteTask }) {
    return (
        <li
            key={task.id}
            className="p-4 bg-gray-50 border rounded-md shadow-sm flex justify-between items-center"
        >
            <div>
                <h3 className="font-bold text-lg text-gray-800">
                    {task.title}
                </h3>
                <p className="text-gray-600">Due Date: {task.due_date}</p>
                <p className="text-gray-600">{task.description}</p>
            </div>
            <div className="space-x-2">
                <button
                    onClick={() => setEditTask(task)}
                    className="bg-blue-500 text-white py-1 px-2 rounded-md hover:bg-blue-600"
                >
                    Edit
                </button>
                <button
                    onClick={() => deleteTask(task.id)}
                    className="bg-red-500 text-white py-1 px-2 rounded-md hover:bg-red-600"
                >
                    Delete
                </button>
            </div>
        </li>
    );
}

export default Task_card;
