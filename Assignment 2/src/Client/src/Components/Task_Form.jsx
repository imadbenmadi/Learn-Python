import React from "react";

function Task_Form({ newTask, handleChange, createTask }) {
    return (
        <form onSubmit={createTask} className="space-y-4">
            <div className="flex flex-col space-y-2">
                <label htmlFor="title" className="text-gray-600">
                    Title
                </label>
                <input
                    type="text"
                    name="title"
                    placeholder="Task Title"
                    value={newTask.title}
                    onChange={handleChange}
                    className="border-gray-300 border rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    required
                />
            </div>

            <div className="flex flex-col space-y-2">
                <label htmlFor="due_date" className="text-gray-600">
                    Due Date
                </label>
                <input
                    type="date"
                    name="due_date"
                    value={newTask.due_date}
                    onChange={handleChange}
                    className="border-gray-300 border rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    required
                />
            </div>

            <div className="flex space-x-4">
                <div className="flex-1">
                    <label htmlFor="type" className="text-gray-600">
                        Type
                    </label>
                    <select
                        name="type"
                        value={newTask.type}
                        onChange={handleChange}
                        className="border-gray-300 border rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    >
                        <option value="personal">Personal</option>
                        <option value="work">Work</option>
                    </select>
                </div>

                {newTask.type === "personal" && (
                    <div className="flex-1">
                        <label htmlFor="priority" className="text-gray-600">
                            Priority
                        </label>
                        <select
                            name="priority"
                            value={newTask.priority}
                            onChange={handleChange}
                            className="border-gray-300 border rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        >
                            <option value="low">Low</option>
                            <option value="medium">Medium</option>
                            <option value="high">High</option>
                        </select>
                    </div>
                )}
            </div>

            <div className="flex flex-col space-y-2">
                <label htmlFor="description" className="text-gray-600">
                    Description
                </label>
                <textarea
                    name="description"
                    placeholder="Task Description"
                    value={newTask.description}
                    onChange={handleChange}
                    className="border-gray-300 border rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
            </div>

            <button
                type="submit"
                className="bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600"
            >
                Create Task
            </button>
        </form>
    );
}

export default Task_Form;
