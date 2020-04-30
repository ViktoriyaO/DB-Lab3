CREATE OR REPLACE VIEW Tables AS
    SELECT
        Diamond.diamond_index,
        Description.color,
        Category.cut,
        Clarity.clarity,
        Diamond.carat_weight
    FROM
        Diamond
        JOIN Description ON Diamond.color = Description.color
        JOIN Category ON Diamond.cut = Category.cut
        JOIN Clarity ON Diamond.clarity = Clarity.clarity;
        
        

