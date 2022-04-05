{% extends "mail_templated/base.tpl" %}

{% block subject %}
Order confirmation from Heiwa - order number {{ order.order_number }}
{% endblock %}

{% block html %}
<h3>Thank you for your order {{ order.full_name }}.</h3>
<strong>Order number -</strong> {{ order.order_number }}
<strong>Order total - </strong>{{ order.order_total }}
<strong>Delivery address -</strong>{{ order.full_address }}.
{% endblock %}