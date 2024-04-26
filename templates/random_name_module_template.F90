module module{{n}}
  use iso_fortran_env, only: REAL64
  implicit none

contains

  ! use jinja2 templating syntax to generate a bunch of subroutines
  ! with different names and the same body

{% for random_string in random_strings -%}
  subroutine {{random_string}}(x, y)
    implicit none
    real(kind=REAL64), intent(in) :: x
    real(kind=REAL64), intent(out) :: y
    y = x * x
  end subroutine {{random_string}}
{% endfor %}

end module module{{n}}
