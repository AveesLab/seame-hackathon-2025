#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"

class SubscriberObject : public rclcpp::Node
{
public:
    SubscriberObject() : Node("cpp_subscriber")
    {
        steer_sub_ = this->create_subscription<std_msgs::msg::Float32>(
            "steer", 10, std::bind(&SubscriberObject::steer_callback, this, std::placeholders::_1));
        throttle_sub_ = this->create_subscription<std_msgs::msg::Float32>(
            "throttle", 10, std::bind(&SubscriberObject::throttle_callback, this, std::placeholders::_1));
    }

private:
    void steer_callback(const std_msgs::msg::Float32::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received steer: %.2f", msg->data);
    }

    void throttle_callback(const std_msgs::msg::Float32::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received throttle: %.2f", msg->data);
    }

    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr steer_sub_;
    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr throttle_sub_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SubscriberObject>());
    rclcpp::shutdown();
    return 0;
}
