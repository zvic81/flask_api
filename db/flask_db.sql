--
-- PostgreSQL database dump
CREATE ROLE flask_user PASSWORD 'flask_user' CREATEDB CREATEROLE INHERIT LOGIN;
CREATE DATABASE flask_db WITH OWNER = flask_user ENCODING = 'UTF-8';
\connect flask_db

-- CREATE TABLE public.goods (
--     id serial PRIMARY KEY,--public.goods_id_seq
--     name character varying(40) NOT NULL,
--     price real,
--     manufacture_date date,
--     picture_url character varying(100)
-- );

-- CREATE TABLE public.orders (
--     id serial PRIMARY KEY, --public.orders_id_seq
--     order_date date,
--     customer_name character varying(40) NOT NULL,
--     customer_email character varying(40),
--     delivery_address character varying(50),
--     status varchar(10),
--     notes character varying(40)
-- );

-- CREATE TABLE public.order_item(
--     id serial PRIMARY KEY,  --public.order_item_id_seq
--     ammount integer NOT NULL,
--     notes character varying(40)
-- );

-- -- ALTER TABLE ONLY public.goods ADD CONSTRAINT goods_pkey PRIMARY KEY (id);
-- ALTER TABLE public.order_item ADD COLUMN order_id INTEGER;
-- ALTER TABLE public.order_item
--     ADD CONSTRAINT fk_orderid
--     FOREIGN KEY (order_id)
--     REFERENCES public.orders(id);
-- ALTER TABLE public.order_item ADD COLUMN good_id INTEGER;
-- ALTER TABLE public.order_item
--     ADD CONSTRAINT fk_goodid
--     FOREIGN KEY (good_id)
--     REFERENCES public.goods(id);
-- ALTER SEQUENCE public.orders_id_seq RESTART WITH 10;
-- ALTER SEQUENCE public.goods_id_seq RESTART WITH 10;
-- ALTER SEQUENCE public.order_item_id_seq RESTART WITH 10;

-- ALTER TABLE public.goods OWNER TO flask_user;
-- ALTER TABLE public.orders OWNER TO flask_user;
-- ALTER TABLE public.order_item OWNER TO flask_user;
-- GRANT ALL ON TABLE public.goods TO flask_user;
-- GRANT ALL ON TABLE public.orders TO flask_user;
-- GRANT ALL ON TABLE public.order_item TO flask_user;
GRANT ALL ON SCHEMA public TO flask_user;


-- INSERT INTO public.goods VALUES (1,'Beer', 112, '05/07/22', 'pic112');
-- INSERT INTO public.goods VALUES (2,'Mushrooms', 12, '05/07/22', 'pic1');
-- INSERT INTO public.goods VALUES (3,'keyboard', 2.5, '05/07/22', 'pickkeybord');
-- INSERT INTO public.goods VALUES (4,'iphone', 199, '2/2/11', 'ya.com');
-- INSERT INTO public.goods VALUES (5,'power supply', 1, '2/2/11', 'fig.com');
-- INSERT INTO public.goods VALUES (6,'mouse', 1000.8, '2/2/11', 'mses.com');

-- INSERT INTO public.orders (id, order_date, customer_name, customer_email, delivery_address, status, notes)
--     VALUES (1,'02/05/2019', 'Sekretov', 'zvic1981@gmail.com', 'Apatity', 'new', 'paid'),
--            (2,'02/05/2019', 'Mihrin',  'zvic1981@gmail.com', 'Kirovsk', 'transact', 'not paid'),
--            (3,'02/05/2019', 'zakharov', 'zakharov@list.ru', 'Apatity', 'paid', 'paid'),
--            (4,'02/05/2019', 'Zelenskiy', 'zelensky@gmail.com', 'Kiyev', 'closed', 'paid'),
--            (5,'02/05/2019', 'Carlson', 'zvic1981@gmail.com', 'Stogholm', 'paid', 'paid');

-- INSERT INTO public.order_item (id, ammount, notes, order_id, good_id)
--     VALUES (1, 4, 'keyboard', 1, 3),
--            (2, 1, 'wifi', 1, 2),
--            (3, 29, 'power', 3, 5),
--            (4, 12, 'iphone', 3, 4);

-- SELECT pg_catalog.setval('public.goods_id_seq', 11, true);


--
-- Name: goods goods_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--
