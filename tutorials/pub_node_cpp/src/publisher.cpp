#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"
#include <chrono>

using namespace std::chrono_literals;

class PublisherObject : public rclcpp::Node
{
public:
    PublisherObject() : Node("cpp_publisher")
    {
        steer_pub_ = this->create_publisher<std_msgs::msg::Float32>("steer", 10);
        throttle_pub_ = this->create_publisher<std_msgs::msg::Float32>("throttle", 10);
        timer_ = this->create_wall_timer(1000ms, std::bind(&PublisherObject::timer_callback, this));
    }

private:
    void timer_callback()
    {
        std_msgs::msg::Float32 steer_msg;
        std_msgs::msg::Float32 throttle_msg;

        steer_msg.data = 0.15;
        throttle_msg.data = -0.3;

        RCLCPP_INFO(this->get_logger(), "Publishing steer: %.2f, throttle: %.2f", steer_msg.data, throttle_msg.data);

        steer_pub_->publish(steer_msg);
        throttle_pub_->publish(throttle_msg);
    }

    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr steer_pub_;
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr throttle_pub_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PublisherObject>());
    rclcpp::shutdown();
    return 0;
}
