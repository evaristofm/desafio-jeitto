SELECT cliente_id,
       count(pedido_id) as total_pedidos
FROM Pedidos
GROUP BY cliente_id
HAVING COUNT(pedido_id) > 5;
