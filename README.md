# CLOUD-MONITORING-AND-ALERTS
"COMPANY": CODTECH IT SOLUTIONS 
"NAME": MOHAMMAD UMAR H
"INTERN ID": CT04DH1951
"DOMAIN": CLOUD COMPUTING 
"DURATION": 4 WEEKS
"MENTOR": NEELA SANTOSH
"Description":The goal is to implement strong observability for a cloud-hosted application. You’ll collect metrics and logs, build visual dashboards, and configure alerting rules using AWS CloudWatch, Google Cloud Monitoring, or Azure Monitor. The final deliverable: a functional dashboard with configured alerts to showcase application health, performance, and timely notifications on issues.


---

1. Data Collection: Metrics & Logs

Metrics: Identify KPIs such as CPU, memory, disk I/O, HTTP request rates, error rates, or latency.

AWS CloudWatch auto-collects AWS service metrics (e.g., EC2 CPUUtilization) and supports custom metrics  .

GCP Monitoring ingests built-in metrics for GCE, Cloud Functions, GKE, and also supports custom or log-based metrics  .


Logs: Stream application/system logs using agents.

On AWS, install the CloudWatch Logs agent to push logs.

In GCP, use Ops Agent to collect and centralize logs for searching and log-based metrics  .




---

2. Dashboard Creation

AWS CloudWatch offers highly customizable dashboards with widgets (graphs, gauges, number/readouts, tables, even alarm grids)  .

You can combine metrics from multiple AWS accounts/regions into one dashboard  .


Google Cloud Monitoring allows dashboards featuring charts for metric data, alerting policy visualizations, and incidents tables  .

Widgets can display alerts, incidents, metrics, logs, and SLOs.


Dashboard best practices:

Focus on key indicators (e.g., error rate, latency, CPU spikes)

Use mixed widget types—trends + current status (gauges, numbers)

Organize layout logically: infrastructure, application, alerts




---

3. Alerting & Notification

AWS CloudWatch Alarms watch metrics (e.g. CPU > 80%) and integrate with SNS for notifications (email, SMS), or even trigger Lambda for automated remediation  .

Alarms can be added directly onto dashboards as widgets  .


GCP Alerting Policies support:

Metrics-based rules (e.g. latency > 2s over 5 minutes)

Log-based alerts for patterns or errors in logs

Forecasted metric conditions for predicted issues  .


Notification channels: email, SMS, Slack, Pub/Sub, webhooks.

In GCP, alert policies generate incidents that show up on dashboards  .




---

4. Sample AWS Implementation Workflow

1. Enable EC2 metrics (CPUUtilization, etc.) and install the CloudWatch Logs agent.


2. Create a CloudWatch Alarm (e.g., CPU>30% for 1 min) tied to an SNS topic/email  .


3. Build a dashboard named MyAppMonitoring: add line graphs for CPU, latency, request count; table widgets for log-based metrics; alarm widgets showing real-time alarm states  .


4. Stress test your app (e.g., via a stress tool or load generator). Observe spikes trigger both dashboard alerts and notifications.




---

5. Sample GCP Implementation Workflow

1. Install Ops Agent on your GCE/GKE resource. Verify that logs and metrics appear in Monitoring.


2. Define custom log-based metrics (e.g., count of error-level logs)  .


3. Set up a metric-based alert policy (e.g., error count > 5 within 5 minutes), and associate with notification channels  .


4. Create a dashboard: include chart widgets for key metrics, an alert policy chart, and an incident table  .




---

6. Deliverable Summary

By completion, you should deliver:

A labeled dashboard showing infrastructure and application health.

Several active alerts with documentation of thresholds and notification targets.

Screenshots or video showing alert triggers and notification delivery.

(Optional) Automation, e.g. SNS-triggered Lambda or GCP Pub/Sub pipelines to archive alerts  .



---

7. Why This Matters

Ensures high reliability through proactive detection.

Enables performance tuning with real-time insights.

Demonstrates applied DevOps/SRE experience for future employers.

Prepares you for the CODTECH internship completion certificate by showcasing a real observability implementation.
"OUTPUT": ![My screenshot](https://user-images.githubusercontent.com/12532091/135541406-7141a8d7-7bf9-4c82-a4d9-ea4b7fe1fb34.jpg)
