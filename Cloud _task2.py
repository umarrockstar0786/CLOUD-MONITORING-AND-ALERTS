resource "aws_cloudwatch_metric_alarm" "cpu_alarm" {
  alarm_name          = "EC2_CPU_High"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300       # 5 minutes
  statistic           = "Average"
  threshold           = 80        # Trigger at ≥ 80% CPU
  alarm_description   = "Alert if EC2 CPU stays at or above 80% for 10 minutes"
  dimensions = {
    InstanceId = var.instance_id  # Set this variable in variables.tf
  }

  actions_enabled = true
  alarm_actions   = [aws_sns_topic.alerts.arn]
  ok_actions      = [aws_sns_topic.alerts.arn]
}
