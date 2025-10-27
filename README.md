# 🌀 Stream Logger Lambda

This AWS Lambda function listens to DynamoDB Streams and logs every change (insert, update, delete) for real-time event tracking. Designed for projects like **GoalForge**, it helps monitor football-related events stored in DynamoDB.

---

## 🚀 Features

- ✅ Triggered by DynamoDB Streams
- ✅ Logs full stream records to CloudWatch
- ✅ Lightweight and beginner-friendly
- ✅ Ready for future enhancements (SNS, S3, etc.)

---

## 📦 File Structure

---

## 🛠️ Setup Instructions

1. **Create DynamoDB Table**
   - Name: `EventPulseTracker`
   - Partition key: `eventId` (String)
   - Enable TTL with attribute `expireAt`
   - Enable Streams: `New and old images`

2. **Deploy Lambda Function**
   - Runtime: Python 3.12
   - Handler: `lambda_function.lambda_handler`
   - Add DynamoDB Stream as trigger
   - Attach `AWSLambdaDynamoDBExecutionRole` policy

3. **Test It**
   - Insert an item into DynamoDB
   - Check CloudWatch Logs for stream output

---

## 📚 Example Stream Record

```json
{
  "eventId": "goal123",
  "player": "Tammy",
  "team": "Lancing FC",
  "expireAt": 1760000000
}
