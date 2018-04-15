# Flexbox Training

## The Display Property

> The first step is to turn an element into a flex container. This is done with two new
values for the well-known display property.

	/* CSS 1 */
	display: inline;
	display: block;
	display: list-item;
	display: none;
	/* CSS 2.1 */
	display: inline-block;
	display: table;
	display: inline-table;
	display: table-row-group;
	display: table-header-group;
	display: table-footer-group;
	display: table-row;
	display: table-column-group;
	display: table-column;
	display: table-cell;
	display: table-caption;
	display: inherit;
	/* Newer display values */
	display: initial;
	display: unset;
	display: flex;
	display: inline-flex;
	display: grid;
	display: inline-grid;
	display: ruby;
	display: ruby-base;
	display: ruby-text;
	display: ruby-base-container;
	display: ruby-text-container;
	/* Experimental values */
	display: run-in;
	display: contents;
	display: inline-list-item;
	display: flow;
	display: flow-root;

> The value of flex turns the element on which it is applied into a block-level flex container box.

> The inline-flex value turns the element on which it is applied into a flex-
container block, but the flex container is an inline-level flex container box.

> Simply adding either of these display property values on an element turns the ele‐
ment into a flex container and the element’s children into flex items. By default, the
children are all the same height, even if their contents would produce elements of different heights.

> The inline-flex value makes the flex container behave like an inline-level element.
It will be only as wide as needed, as declared.

> Like other inline-level elements, the
inline-flex container sits together on a line with other inline-level elements, and is
affected by the line-height and vertical alignment, which creates space for the
descenders underneath the box by default.

## Flex Container

> The first important notion to fully understand is that of flex container, also known as container box. The element on which display: flex or display: inline-flex is applied becomes a flex formatting context for the containing box’s children, known as the flex container. Once we have created a flex container (by adding a display: flex or display: inline-flex ), we need to learn how to manipulate the layout of the container’s children.

### Flex Container Properties

> Sometimes we’ll have one flex item, sometimes we’ll have dozens. Sometimes we’ll know how many children a node will have. Sometimes the number of children will not be under our control. We might have a varied number of items in a set-width container. We might know the number of items, but not know the width of the container.

> The display , flex-direction , flex-wrap , and flex-flow properties impact the ordering and orientation of the flex container. The justify-content , align-items , and align-content properties can be applied to the flex container to impact the alignment of the container’s children.

#### The flex-flow Shorthand Property

> The flex-flow property lets you define the directions of the main and cross axes and
whether the flex items can wrap to more than one line if needed

	Values: <flex-direction> || <flex-wrap>

	Initial value: row nowrap

> The flex-flow shorthand property sets the flex-direction and flex-wrap proper‐
ties to define the flex container’s wrapping and main and cross axes.

> The default value of flex-direction is row . The default value of flex-wrap is now
rap .

##### The flex-direction Property

> If you want your layout to go from top to bottom, left to right, right to left, or even
bottom to top, you can use flex-direction to control the main axis along which the
flex items get laid out.

	Values: row | row-reverse | column | column-reverse
	
	Initial value: row

> The flex-direction property specifies how flex items are placed in the flex container.

	row - left to right
	row-reverse - right to left
	column - top to bottom
	column-reverse - bottom to top