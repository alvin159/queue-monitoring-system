# Queue Monitoring System

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/queue-monitoring-system.git
   cd queue-monitoring-system
   cd backend
   ```

2. **Install the dependecies:**

   ```bash
   npm install
   ```

3. **Set up the environment:**
Replace <username> and <password> in .env file with alvinasw159:

   ```env
   MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/'queue_app?retryWrites=true&w=majority

   ```

4. **Start the server:**

   ```bash
   npm start
   ```
The server will run on http://localhost:5000.


**Example: POST Request**
Use curl to post data to the server:

   ```bash
    curl -X POST http://localhost:5000/api/queues -H "Content-Type: application/json" -d "{\"id\":\"12345\", \"company_id\":\"XYZ\", \"store_id\":\"StoreA\", \"queue_length\":15, \"confidence\":0.95}"
   ```

Response (example) on http://localhost:5000/api/queues:

   ```json
    {
        "id": "12345",
        "company_id": "XYZ",
        "store_id": "StoreA",
        "queue_length": 15,
        "confidence": 0.95,
        "_id": "67e42e5ce061a71962ba4ff7",
        "timestamp": "2025-03-26T16:42:04.532Z",
        "__v": 0
    }

   ```
