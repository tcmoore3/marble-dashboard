from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer, VideoViewer
from signac_dashboard.modules import Notes
import signac


class PlotDashboard(Dashboard):
    def job_sorter(self, job):
        return [job.sp.phi, job.sp.kT]

    def job_title(self, job):
        pressure = 'p.f. = {}'.format(job.sp.phi)
        kT = 'kT = {}'.format(job.sp.kT)
        replica = 'rep {}'.format(job.sp.replica)
        return '; '.join((pressure, kT, replica))


if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    img_globs = []
    for img_glob in img_globs:
        mod_name = img_glob.replace('-', ' ').replace('.png', '').capitalize()
        modules.append(
                ImageViewer(
                    img_globs=[img_glob],
                    name=mod_name,
                )
        )
    modules.append(ImageViewer(img_glob='test-fresnel-render.png', name='Color by hexatic order'))
    modules.append(ImageViewer(img_glob='color-by-bonds.png', name='Color by number of bonds'))
    notes_mod = Notes(name='Structure', key='structure')
    #notes_mod = Notes(name='Keep running?', key='keep_running')
    #modules.append(notes_mod)
    config = {'PER_PAGE': 50}
    pr = signac.get_project('/gpfs/alpine/mat110/proj-shared/patchy-polygons')
    PlotDashboard(config=config, modules=modules, project=pr).main()
