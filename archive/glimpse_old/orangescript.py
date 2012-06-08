#!/usr/bin/env python

# This script takes a set of training/testing feature vectors from a glab
# experiment, and writes them to disk as an Orange Table file.

from glimpse.glab import Experiment
from glimpse import util
import warnings
with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  import Orange
import sys

def MakeOrangeTableFromExperiment(classes, all_features, all_image_paths, whole_set):
  # all_features contains a list of 2D numpy arrays: organized by class, then
  # image, then feature.
  num_classes = len(all_features)
  assert num_classes > 0
  assert all(len(ftrs_per_image) > 0 for ftrs_per_image in all_features)
  num_features = all_features[0].shape[1]
  assert num_features > 0
  assert all(ftrs_per_image.shape[1] == num_features
      for ftrs_per_image in all_features)
  all_features = [ map(list, cls_ftrs) for cls_ftrs in all_features ]
  it_attributes = [ Orange.data.variable.Continuous("f%d" % x)
      for x in range(num_features) ]
  img_path_attribute = Orange.data.variable.String("img_path")
  cls_attribute = Orange.data.variable.Discrete("cls", values = classes)
  domain = Orange.data.Domain(it_attributes, cls_attribute)
  meta_id = Orange.data.new_meta_id()
  domain.add_meta(meta_id, img_path_attribute)
  for cls, cls_ftrs, cls_imgs in zip(classes, all_features, all_image_paths):
    for img_ftrs, img_path in zip(cls_ftrs, cls_imgs):
      img_ftrs += [cls]
  all_features = util.UngroupLists(all_features)
  table = Orange.data.Table(domain, all_features)
  idx = 0
  for cls_imgs in all_image_paths:
    for img_path in cls_imgs:
      table[idx][img_path_attribute] = img_path
      idx += 1
  return table

def main():
  whole_set = False
  if len(sys.argv) < 3:
    sys.exit("usage: %s GLIMPSE-EXPERIMENT.dat ORANGE-TRAIN-DATA.tab ORANGE-TEST-DATA.tab" % sys.argv[0])
  if len(sys.argv) is 3:
    ifname, train_ofname = sys.argv[1:3]
    whole_set = True
  else:
    ifname, train_ofname, test_ofname = sys.argv[1:4]
    whole_set = False
  exp = Experiment.Load(ifname)
  train_table = MakeOrangeTableFromExperiment(exp.classes, exp.train_features, exp.train_images)
  train_table.save(train_ofname)
  test_table = MakeOrangeTableFromExperiment(exp.classes, exp.test_features, exp.test_images)
  test_table.save(test_ofname)

main()
