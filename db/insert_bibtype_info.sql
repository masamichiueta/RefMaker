INSERT INTO `bibtype` (`id`, `name`)
VALUES
    (1, 'article'),
    (2, 'book'),
    (3, 'booklet'),
    (4, 'inbook'),
    (5, 'incollection'),
    (6, 'inproceedings'),
    (7, 'conference'),
    (8, 'manual'),
    (9, 'mastersthesis'),
    (10, 'phdthesis'),
    (11, 'proceedings'),
    (12, 'techreport'),
    (13, 'unpublished'),
    (14, 'misc');

INSERT INTO `must_item` (`id`, `type_id`, `item_name`)
VALUES
    (1, 1, 'author'),
    (2, 1, 'journal'),
    (3, 1, 'title'),
    (4, 1, 'year'),
    (5, 2, 'author/editor'),
    (6, 2, 'title'),
    (7, 2, 'publisher'),
    (8, 3, 'title'),
    (9, 4, 'author/editor'),
    (10, 4, 'chapter/pages'),
    (11, 4, 'publisher'),
    (12, 4, 'title'),
    (13, 4, 'year'),
    (14, 5, 'author'),
    (15, 5, 'booktitle'),
    (16, 5, 'publisher'),
    (17, 5, 'title'),
    (18, 5, 'year'),
    (19, 6, 'author'),
    (20, 6, 'booktitle'),
    (21, 6, 'title'),
    (22, 6, 'year'),
    (23, 7, 'author'),
    (24, 7, 'booktitle'),
    (25, 7, 'title'),
    (26, 7, 'year'),
    (27, 8, 'title'),
    (28, 9, 'author'),
    (29, 9, 'school'),
    (30, 9, 'title'),
    (31, 9, 'year'),
    (32, 10, 'author'),
    (33, 10, 'school'),
    (34, 10, 'title'),
    (35, 10, 'year'),
    (36, 11, 'title'),
    (37, 11, 'year'),
    (38, 12, 'author'),
    (39, 12, 'title'),
    (40, 12, 'institution'),
    (41, 12, 'year'),
    (42, 13, 'author'),
    (43, 13, 'title'),
    (44, 13, 'note');
