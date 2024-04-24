module module{{n}}
  use iso_fortran_env, only: REAL64
  implicit none

contains

  ! use jinja2 templating syntax to generate a bunch of subroutines
  ! with different names and the same body

{% for n in range(1, n+1) -%}
{% for i in range(1, num_subs+1) -%}
  subroutine sub{{n}}_{{i}}(x, y)
    implicit none
    real(kind=REAL64), intent(in) :: x
    real(kind=REAL64), intent(out) :: y
    y = x * x
  end subroutine sub{{n}}_{{i}}
{% endfor %}
{% endfor %}
  

end module module{{n}}
