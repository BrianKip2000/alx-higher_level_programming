-- maximum for states
SELECT state, MAX(value) AS state_max FROM temperatures GROUP BY state ORDER BY state;
