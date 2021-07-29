import numpy as np
import meshio
import glob
import os

expected_formats = ["stl", "obj", "e", "txt"]


def change_mesh_format(in_mesh: str, out_format: str, out_mesh: str = None):
    assert os.path.exists(in_mesh)
    assert out_format in expected_formats

    mesh = meshio.read(in_mesh)
    if out_mesh is not None:
        out_mesh_name = out_mesh
    else:
        handle = in_mesh.split(".")[0]
        out_mesh_name = handle + "." + out_format

    if out_format == "txt":
        mesh_as_array = mesh_to_array(mesh)
        np.savetxt(out_mesh_name, mesh_as_array, delimiter=" ", fmt="%.4f")

    else:
        mesh.write(out_mesh_name, file_format=out_format)


def mesh_to_array(mesh: meshio.Mesh):
    assert "triangle" in mesh.cells_dict.keys()
    triangles = mesh.cells_dict["triangle"]
    point_dict = {i: point for i, point in enumerate(mesh.points)}
    mesh_as_array = np.array([np.hstack([point_dict[vertex] for vertex in tri]) for tri in triangles])
    return mesh_as_array


def convert_multi(search_string: str, out_format: str):
    files = list(glob.glob(search_string))
    assert len(files) > 0
    for fname in files:
        change_mesh_format(fname, out_format)