-- FATURAMENTO POR CATEGORIA

SELECT

Categoria,

SUM(Total) AS Faturamento

FROM vendas

GROUP BY Categoria

ORDER BY Faturamento DESC;



-- FATURAMENTO POR CIDADE

SELECT

Cidade,

SUM(Total) AS Faturamento

FROM vendas

GROUP BY Cidade

ORDER BY Faturamento DESC;



-- TOP 10 CLIENTES

SELECT

Cliente,

SUM(Total) AS Total

FROM vendas

GROUP BY Cliente

ORDER BY Total DESC

LIMIT 10;



-- TOP 10 PRODUTOS

SELECT

Produto,

SUM(Total) AS Total

FROM vendas

GROUP BY Produto

ORDER BY Total DESC

LIMIT 10;



-- QUANTIDADE DE VENDAS

SELECT

COUNT(*) AS TotalVendas

FROM vendas;



-- TICKET MÉDIO

SELECT

ROUND(AVG(Total),2) AS TicketMedio

FROM vendas;



-- FATURAMENTO TOTAL

SELECT

ROUND(SUM(Total),2) AS Faturamento

FROM vendas;



-- VENDAS POR MÊS

SELECT

strftime('%Y-%m',Data) AS Mes,

SUM(Total) AS Faturamento

FROM vendas

GROUP BY Mes

ORDER BY Mes;